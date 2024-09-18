import os
import keyboard
import time

def list_devices():
    devices = os.popen("adb devices").read().strip().splitlines()
    devices = [device.split()[0] for device in devices[1:] if "device" in device]
    
    if not devices:
        print("No devices found. Please connect a device.")
        return None
    else:
        print("List of connected devices:")
        for i, device in enumerate(devices):
            print(f"{i+1}. {device}")
        return devices

def choose_device(devices):
    while True:
        try:
            choice = int(input("Enter the number of the device you want to choose: ")) - 1
            if 0 <= choice < len(devices):
                return devices[choice]
            else:
                print("Invalid choice. Please choose a valid device number.")
        except ValueError:
            print("Please enter a valid number.")

def reboot_to_recovery(device):
    result = os.popen(f"adb -s {device} reboot recovery").read()
    print(f"Rebooting device {device} into recovery mode...")
    print(result)
    time.sleep(10)  # Give time for the device to enter recovery mode
    print(f"Device {device} should now be in recovery mode.")

def bypass_frp(device):
    while True:
        print(f"Checking FRP bypass status on device {device}...")
        result = os.popen(f"adb -s {device} shell content insert --uri content://settings/secure --bind name:s:user_setup_complete --bind value:s:1").read()
        print(f"FRP bypass result on device {device}: {result}")
        time.sleep(5)  # Wait a bit before the next check
        if keyboard.is_pressed("q"):
            print("Exiting FRP bypass mode...")
            break

def monitor_device_insertion_recovery():
    print("Monitoring for new devices and rebooting to recovery mode...")
    last_devices = []
    while True:
        devices = list_devices()
        if devices and devices != last_devices:
            print(f"New device detected: {devices[0]}")
            reboot_to_recovery(devices[0])
            last_devices = devices
            break  # If you don't wanna to get back to the options remove the `break`
        time.sleep(2)  # Check every 2 seconds for new devices

def monitor_device_insertion_frp():
    print("Monitoring for new devices and bypassing FRP...")
    while True:
        devices = list_devices()
        if devices:
            print(f"New device detected: {devices[0]}")
            bypass_frp(devices[0])
        time.sleep(2)  # Check every 2 seconds for new devices

def main():
    while True:
        print("\nOptions:")
        print("1. List connected devices")
        print("2. Reboot device into recovery mode")
        print("3. Continuously bypass FRP on inserted device")
        print("4. Continuously reboot inserted device into recovery mode")
        print("5. Exit")

        choice = input("Choose an option: ")
        
        if choice == "1":
            devices = list_devices()
            if devices:
                print("Devices listed successfully.")
        
        elif choice == "2":
            devices = list_devices()
            if devices:
                device = choose_device(devices)
                reboot_to_recovery(device)

        elif choice == "3":
            monitor_device_insertion_frp()

        elif choice == "4":
            monitor_device_insertion_recovery()

        elif choice == "5":
            print("Exiting script.")
            break
        
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
