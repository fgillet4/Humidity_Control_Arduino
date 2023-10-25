# Humidity Control Arduino on Raspberry Pi

This README guides you on how to manage and monitor the Humidity Control Arduino service running on a Raspberry Pi. You can both use the `screen` method to run it interactively and the systemd service to run it as a background process.

## Using `screen`:

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



