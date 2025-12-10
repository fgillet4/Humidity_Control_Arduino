# Install Python Packages

`pip install Flask pyserial threading jsonify`

Python version 3.11

# Raspberry Pi Headless Setup Guide

<<<<<<< HEAD
After flashing the Raspberry Pi OS onto an SD card using tools like Etcher, follow these steps to set up your Pi for headless access (without a monitor).
=======
After flashing the Raspberry Pi OS onto an SD card using tools like Etcher, follow these steps to set up your Pi for headless access (without a monitor). For quickst SSH only set up try

32-bit OS lite (no desktop, cli only)
64-bit OS lite (no desktop, uses more RAM)

Setting this up is faster on Raspberry Pi Imager
>>>>>>> 7e1709e (asd)

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

<<<<<<< HEAD
ssh pi@raspberrypi.local

=======
```bash
ssh pi@raspberrypi.local
ssh pi@xxx.xxx.x.xxx 
```
Try using the ip address of the Pi if this doesnt work
>>>>>>> 7e1709e (asd)
The default password is `raspberry`.

## 5. Setting a Secure Password

For enhanced security, it's recommended to change the default password to something unique. You can generate a secure password hash using:
```bash
echo 'your_password' | openssl passwd -6 -stdin
```
This command will provide you with a hashed version of your password. Use this hash when setting up password authentication in relevant configuration files.

<<<<<<< HEAD

=======
## Port Forwarding to the Pi
For SSH access via the internet, you need to set up port forwarding to direct incoming SSH connections from the WAN side (the internet) to the specific internal IP address (the device within your local network that runs the SSH server, such as a Raspberry Pi).

Here's what a typical SSH port forwarding setup should include:

Name/Description: A descriptive name for the service (e.g., "SSH for Raspberry Pi").

Protocol: TCP (Transmission Control Protocol), since SSH uses TCP.

WAN Port: This is the external port number that you would use to connect to your device from outside your local network. It's a good security practice to choose a non-standard port number (not 22) to avoid automated attacks. For example, you might choose port 2224 as in your screenshot.

LAN Port: This is the internal port that the SSH service listens to on your device. By default, SSH listens on port 22.

Destination IP: The internal IP address of the device you want to connect to. This should be the static IP address of your Raspberry Pi or other devices that you're SSH-ing into, such as 192.168.1.130.

Destination MAC: This field is usually optional and is sometimes filled in automatically by the router for ease of management. It identifies the hardware address of the network interface of the destination device.

If the router's interface allows you to enable or disable rules, make sure your SSH rule is enabled.

Example Configuration for SSH:

Name: SSH for Raspberry Pi
Protocol: TCP
WAN Port: 2224 (or any port you prefer that isn't commonly used)
LAN Port: 22
Destination IP: 192.168.1.130 (the static IP of your Raspberry Pi)
Destination MAC: [Filled in if required or automatically detected]
To connect from outside your network, you'd use the external IP address of your router and the WAN port number. For example:

```bash
ssh -p 2224 user@external-ip-address
```

## Security Considerations

Consider setting up fail2ban
Setting up a security measure like fail2ban is a good practice when exposing your Raspberry Pi to the internet via SSH. fail2ban works by monitoring log files for failed login attempts and automatically bans IPs that show malicious signs such as too many password failures.

Here’s how to set up fail2ban on your Raspberry Pi:

Install fail2ban:

```bash
sudo apt update
sudo apt install fail2ban
```
# Configure fail2ban:

Copy the default configuration file to create a new custom configuration file:
bash
Copy code
sudo cp /etc/fail2ban/jail.conf /etc/fail2ban/jail.local
Edit the jail.local file to set up your policies:
bash
Copy code
sudo nano /etc/fail2ban/jail.local
Here are some common settings to configure:
bantime: the duration an IP is banned for after failing to log in correctly.
findtime: the time frame during which multiple failed login attempts trigger a ban.
maxretry: the number of failed login attempts allowed within the findtime before an IP is banned.
Here’s an example of what you might add under the [sshd] section in jail.local:

ini
Copy code
[sshd]
enabled = true
port = ssh
filter = sshd
logpath = /var/log/fail2ban.log
bantime = 3600 # 1 hour
findtime = 600 # 10 minutes
maxretry = 3
Activate fail2ban:

After you’ve configured your settings, save the file and restart the fail2ban service to apply the changes:
bash
Copy code
sudo systemctl restart fail2ban
Check fail2ban status:

To check the status of fail2ban and see which IPs have been banned, use:
bash
Copy code
sudo fail2ban-client status sshd
Additional Security Measures:

Use SSH Keys: Instead of passwords, use SSH key-based authentication for added security.
Disable Password Authentication: Once you have key-based authentication set up, disable password authentication in your SSH configuration (/etc/ssh/sshd_config) to prevent brute-force password attacks.

Delete and start over:
```bash
sudo apt-get purge fail2ban
sudo apt-get install fail2ban
```

Troubleshoot:
check that log in jail.local matches with /var/log/
sudo tail -f /var/log/fail2ban.log
sudo systemctl status fail2ban
ls -l /var/run/fail2ban/fail2ban.sock
sudo tail -n 50 /var/log/fail2ban.log
sudo journalctl -u fail2ban
sudo fail2ban-server -f -x
>>>>>>> 7e1709e (asd)


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
# Raspberry Pi DDNS Client Setup Instructions

Follow these steps to set up Dynamic DNS on your Raspberry Pi, which will keep your network accessible through a fixed hostname despite a changing public IP address.

## Prerequisites

* A Raspberry Pi running Raspberry Pi OS
* An internet connection
* A DDNS account (e.g., No-IP)

## Installation and Configuration

### 1. Update Your System

Ensure your Raspberry Pi is up to date:

```shell
sudo apt update
sudo apt upgrade
```

## *2. Install DDclient
Install the `ddclient` package:

```shell
sudo apt install ddclient
```

## *3. Configure DDclient
Install the `ddclient` package:

```shell
sudo nano /etc/ddclient.conf
```

Add your DDNS service configuration:

```
protocol=dyndns2
use=web, web=checkip.dyndns.com/, web-skip=/"IP Address"/
server=dynupdate.no-ip.com
login=your_noip_login
password=/your_noip_password/
your_noip_hostname
```
Make sure to replace your_noip_login, /your_noip_password/, and your_noip_hostname with your actual No-IP credentials and hostname.

## *4. Enable and Start the DDclient Service
Enable `ddclient` to start on boot:

```shell
sudo systemctl enable ddclient
```
Start the `ddclient` service:


```shell
sudo systemctl start ddclient
```

## *5. Testing the Configuration

Force an immediate update with:


```shell
sudo ddclient -force
```
Start the `ddclient` service:

## *6. Check for Errors

Review the `ddclient` logs if needed:

```shell
grep ddclient /var/log/syslog
```
