# Tablet Automation Toolkit

A simple toolkit for automating tablet operations like rebooting into recovery mode and bypassing FRP (Factory Reset Protection) on Android devices, specifically for Huawei and Lenovo tablets.

## Features
- List connected devices via ADB.
- Reboot selected devices into recovery mode.
- Continuously bypass FRP when a device is connected.

## Installation

### Prerequisites
1. **ADB (Android Debug Bridge)**: Make sure ADB is installed and accessible via your system's PATH.
   - You can download ADB from the official Android developer site: [ADB Download](https://developer.android.com/studio/command-line/adb).

2. **Python 3.x**: This script requires Python 3.x to run.
   - You can download Python from: [Python Download](https://www.python.org/downloads/)

3. **ADB Permissions**: Ensure your devices have USB debugging enabled and proper ADB permissions are granted.

### Step-by-Step Setup

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/johntad110/Tablet-Automation-Toolkit.git
   cd Tablet-Automation-Toolkit
   ```

2. Install the required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. Ensure that ADB is properly set up and devices are connected with USB debugging enabled.

## Usage

1. Open a terminal/command prompt and navigate to the project directory.
2. Run the script:
   ```bash
   python main.py
   ```

3. Select one of the options from the menu:
   - **List Devices**: Displays a list of all connected devices.
   - **Reboot to Recovery Mode**: Allows you to choose a device and reboot it into recovery mode.
   - **Bypass FRP Mode**: Automatically bypasses FRP when a new device is detected.

### Exiting the script
You can press `Ctrl + C` or choose the exit option in the menu to stop the script.

### Notes
- **ADB Drivers**: Ensure that the correct ADB drivers for your device are installed on your computer.
- **FRP Bypass**: The FRP bypass command only works when the device is in the correct mode (e.g., fastboot, recovery, or while setting up a new device).

## Requirements

Ensure you have the following dependencies installed. These can also be found in the `requirements.txt` file:

```txt
keyboard
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
