# Install Python Packages

`pip install Flask pyserial threading jsonify`

Python version 3.11

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




# How to Detach the Flask Server from the SSH Session

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
    ssh raspberrypi@raspberrypi.local
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

## Use systemd to restart the Web Server upon reboot of the Pi:

`humidity-control.service` should already be in the directory

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
# Arduino Command Line Interface (CLI) Setup on Raspberry Pi

Follow these steps to install, set up, and use the `arduino-cli` on the Raspberry Pi to compile and upload sketches to your Arduino board. The use of this is to be able to change or upload new arduino sketches from ssh. Make sure you are ssh'd into the Pi.

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

# Setting Up Custom Hostname on Raspberry Pi

## **1. Setting up Raspberry Pi**

- Start with a fresh install of Raspberry Pi OS (formerly Raspbian) on your Raspberry Pi.

## **2. Boot up and connect**

- Once you've booted up, connect to your Raspberry Pi either directly (using a monitor, keyboard, etc.) or SSH into it using its default hostname:

  ```bash
  ssh pi@raspberrypi.local
  ```

  > Default password is usually `raspberry`.

## **3. Change the hostname**

- Once connected, edit the `hostname` file:

  ```bash
  sudo nano /etc/hostname
  ```

  - Replace the default name `raspberrypi` with your desired name. For this guide, we'll use `krypgrund` which means "crawlspace" in Swedish, you can use any name you like.

- Next, update the `hosts` file:

  ```bash
  sudo nano /etc/hosts
  ```

  - Find the line that reads `127.0.1.1 raspberrypi` and change `raspberrypi` to `krypgrund`.

## **4. Reboot the Raspberry Pi**

- For the changes to take effect, reboot the Raspberry Pi:

  ```bash
  sudo reboot
  ```

## **5. Connect using the new hostname**

- After the reboot, you can now SSH into your Raspberry Pi using the new hostname:

  ```bash
  ssh pi@krypgrund.local
  ```

  > Remember to use the password you've set previously.

## **6. All done!**

- Your Raspberry Pi is now accessible via the new hostname `krypgrund.local`.

# Changing Default SSH Username on Raspberry Pi

## **1. Log into your Raspberry Pi**

- Start by SSHing into your Raspberry Pi using the default credentials:

  ```bash
  ssh pi@krypgrund.local
  ```

  > Default password is usually `raspberry`.

## **2. Create a new user**

- Once logged in, add a new user called `krypgrund`:

  ```bash
  sudo adduser krypgrund
  ```

  - Follow the prompts to set a password and provide any additional information (or just press enter for defaults).

## **3. Grant the new user sudo privileges**

- To ensure the new user can perform administrative tasks, add them to the `sudo` group:

  ```bash
  sudo usermod -aG sudo krypgrund
  ```

## **4. Test the new user**

- Before making any further changes, SSH into the Raspberry Pi using the new user to ensure everything is working:

  ```bash
  ssh krypgrund@krypgrund.local
  ```

  > Enter the password you set for `krypgrund` when prompted.

## **5. Disable the default `pi` user**

- For security reasons, it's a good idea to disable the default `pi` user once you're certain your new user works:

  ```bash
  sudo passwd -l pi
  ```

  This locks the `pi` account.

## **6. All done!**

- You've successfully changed the default SSH user. Now you can log in with:

  ```bash
  ssh krypgrund@krypgrund.local
  ```


