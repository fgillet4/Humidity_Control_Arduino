# Raspberry Pi Headless Setup Guide

After flashing the Raspberry Pi OS onto an SD card using tools like Etcher, follow these steps to set up your Pi for headless access (without a monitor).

## 1. Enable SSH Access

To enable SSH access:
- Create an empty file named `ssh` (with no file extension) and place it in the root directory of the boot partition.

## 2. Set Up WiFi (Optional)

Note:Make sure the wifi you are using is 2.4 GHz since the pi only supports 2.4 GHz

If you want your Raspberry Pi to connect to your WiFi network on boot:
1. Create a file named `wpa_supplicant.conf` in the root directory of the boot partition.
2. Add the following content, replacing with your actual WiFi details:
```
country=US
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1

network={
ssid="YOUR_WIFI_SSID"
psk="YOUR_WIFI_PASSWORD"
key_mgmt=WPA-PSK
}
```

Ensure to replace `YOUR_WIFI_SSID` and `YOUR_WIFI_PASSWORD` with your WiFi credentials. If you're not in the US, adjust the `country` field accordingly.

## 3. Safely Eject the SD Card

- Ensure you safely eject the SD card from your computer.

## 4. Boot Your Raspberry Pi

- Insert the SD card into the Raspberry Pi and power it on.
- After it's booted up, you can access your Raspberry Pi via SSH from another computer on the same network using:

ssh pi@raspberrypi.local

The default password is `raspberry`.

## 5. Setting a Secure Password

For enhanced security, it's recommended to change the default password to something unique. You can generate a secure password hash using:
```bash
echo 'your_password' | openssl passwd -6 -stdin
```
This command will provide you with a hashed version of your password. Use this hash when setting up password authentication in relevant configuration files.




# Humidity Control Arduino on Raspberry Pi

This README guides you on how to manage and monitor the Humidity Control Arduino service running on a Raspberry Pi. You can both use the `screen` method to run it interactively and the systemd service to run it as a background process.

## Using `screen`:

### **Installing `screen`:**
```bash
sudo apt-get update
sudo apt-get install screen
```

### **Starting the Script with `screen`:**

1. SSH into your Raspberry Pi:
    ```bash
    ssh krypgrund@krypgrund.local
    ```

2. Start a new `screen` session named "arduino":
    ```bash
    screen -S arduino
    ```

3. Run the script:
    ```bash
    sudo python3 web_server.py
    ```

4. Detach from the `screen` session with `CTRL` + `A` followed by `CTRL` + `D`.

### **Re-attaching to the `screen`:**

If you want to see the live output or interact with the running script:
```bash
screen -r arduino
```

## Using systemd:

### **Starting the Service:**
```bash
sudo systemctl start humidity-control.service
```

### **Stopping the Service:**
```bash
sudo systemctl stop humidity-control.service
```
### **Restarting the Service:**
```bash
sudo systemctl restart humidity-control.service
```
### **Status of the Service:**
```bash
sudo systemctl status humidity-control.service
```
# Arduino CLI Setup on Raspberry Pi

Follow these steps to install, set up, and use the `arduino-cli` on the Raspberry Pi to compile and upload sketches to your Arduino board.

## 1. Installing `arduino-cli`

Download and install the `arduino-cli`:
```bash
curl -fsSL https://raw.githubusercontent.com/arduino/arduino-cli/master/install.sh | sh
```

## 2. Update $PATH

Append the installation directory of `arduino-cli` to your `~/.bashrc`:
```bash
echo 'export PATH="$PATH:/home/krypgrund/krypgrund/bin"' >> ~/.bashrc
```
Reload your `~/.bashrc`:
```bash
source ~/.bashrc
```

## 3. Initialize Configuration

Initialize a new configuration file:
```bash
arduino-cli config init
```

## 4. Update Core Index

Fetch the latest list of available platforms:
```bash
arduino-cli core update-index
```

## 5. Installing Arduino Core

(Note: Additional instructions to be added based on the specific core or other requirements.)



