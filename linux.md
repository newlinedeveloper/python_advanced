### **Shell Scripting and Unix Commands**

#### **Shell Scripting**

**Shell scripting** is writing scripts for the shell, a command-line interpreter in Unix/Linux systems. These scripts automate tasks by executing a series of commands.

**Basic Structure of a Shell Script**:
1. **Shebang** (`#!`): Specifies the interpreter to be used.
2. **Commands**: The sequence of commands to be executed.
3. **Variables**: Used to store data.
4. **Control Structures**: Like loops and conditionals.

**Example**: A script to back up a directory.
```bash
#!/bin/bash

# Variables
SOURCE_DIR="/path/to/source"
BACKUP_DIR="/path/to/backup"

# Create a backup
cp -r "$SOURCE_DIR" "$BACKUP_DIR"

echo "Backup completed from $SOURCE_DIR to $BACKUP_DIR"
```

**Features**:
- **Comments**: Start with `#`.
- **Executing Scripts**: Make the script executable and run it.
  ```bash
  chmod +x backup.sh
  ./backup.sh
  ```

---

#### **Unix Commands**

Unix commands are powerful tools for file management, process control, system monitoring, and more. Below are some commonly used commands:

1. **File Management**:
   - `ls`: List directory contents.
     ```bash
     ls -l
     ```
   - `cp`: Copy files or directories.
     ```bash
     cp file1.txt file2.txt
     ```
   - `mv`: Move or rename files.
     ```bash
     mv oldname.txt newname.txt
     ```
   - `rm`: Remove files or directories.
     ```bash
     rm file.txt
     ```
   - `find`: Search for files in a directory hierarchy.
     ```bash
     find /path -name "*.txt"
     ```

2. **Process Control**:
   - `ps`: Display currently running processes.
     ```bash
     ps aux
     ```
   - `top`: Real-time view of system resource usage.
     ```bash
     top
     ```
   - `kill`: Terminate a process by PID.
     ```bash
     kill 1234
     ```

3. **System Monitoring**:
   - `df`: Report disk space usage.
     ```bash
     df -h
     ```
   - `du`: Estimate file space usage.
     ```bash
     du -sh /path/to/directory
     ```
   - `uptime`: Show how long the system has been running.
     ```bash
     uptime
     ```

**Advanced Concepts**:
- **Piping and Redirection**: Sending the output of one command as input to another.
  ```bash
  ls -l | grep ".txt"
  ```
- **Cron Jobs**: Schedule tasks to run at specific intervals.
  ```bash
  crontab -e
  ```

**Example**: A script to clean up old log files.
```bash
#!/bin/bash

# Variables
LOG_DIR="/var/log/myapp"
DAYS=30

# Find and delete files older than 30 days
find "$LOG_DIR" -type f -mtime +$DAYS -exec rm -f {} \;

echo "Old log files deleted from $LOG_DIR"
```
---

## **1️⃣ System Administration & Troubleshooting**
### **Q1: How do you check system resource usage (CPU, memory, disk, network) on Linux?**  
✅ **Answer:**  
You can use the following commands:  
```bash
top        # Shows real-time CPU and memory usage
htop       # Similar to top, but more user-friendly
free -m    # Check available memory in MB
df -h      # Check disk space usage
iostat     # View CPU and disk I/O statistics
vmstat 1   # Display system performance (CPU, memory, I/O)
```

---

### **Q2: How do you troubleshoot high CPU usage on a Linux server?**  
✅ **Answer:**  
1. **Find the processes consuming the most CPU:**  
   ```bash
   top      # Press 'P' to sort by CPU usage
   htop     # Alternative to 'top'
   ps aux --sort=-%cpu | head -10  # List top 10 CPU-consuming processes
   ```
2. **Check if a process is stuck or looping:**  
   ```bash
   strace -p <PID>   # View system calls made by the process
   ```
3. **Kill or restart the process if necessary:**  
   ```bash
   kill -9 <PID>  # Forcefully kill process
   systemctl restart <service>  # Restart a service
   ```

---

### **Q3: A process is consuming too much memory, how would you debug it?**  
✅ **Answer:**  
1. **Find high memory-consuming processes:**  
   ```bash
   ps aux --sort=-%mem | head -10
   ```
2. **Check real-time memory usage:**  
   ```bash
   free -m
   ```
3. **Check memory leaks using `pmap`:**  
   ```bash
   pmap <PID> | tail -n 1
   ```
4. **Restart or kill the process if needed:**  
   ```bash
   kill -9 <PID>
   ```

---

### **Q4: How do you check which ports are open and which services are listening?**  
✅ **Answer:**  
```bash
netstat -tulnp  # Lists all open ports with processes
lsof -i         # Shows which processes are using network ports
ss -tulnp       # Faster alternative to netstat
```

---

### **Q5: How do you restart a crashed service automatically?**  
✅ **Answer:**  
Use `systemd` to restart services automatically:  
```bash
sudo systemctl edit <service>
```
Add the following lines:  
```
[Service]
Restart=always
RestartSec=5
```
Then reload systemd:  
```bash
sudo systemctl daemon-reload
sudo systemctl restart <service>
```

---

## **2️⃣ File System & Storage**
### **Q6: How do you find the largest files consuming disk space?**  
✅ **Answer:**  
```bash
du -ah / | sort -rh | head -10
```

---

### **Q7: How do you mount a disk in Linux?**  
✅ **Answer:**  
```bash
mount /dev/sdX /mnt
```
For permanent mounting, add an entry in `/etc/fstab`.

---

## **3️⃣ Networking & Security**
### **Q8: How do you check your system’s IP address and default gateway?**  
✅ **Answer:**  
```bash
ip a        # Show all IP addresses
ip route    # Show default gateway
```

---

### **Q9: How do you test if a remote server is reachable?**  
✅ **Answer:**  
```bash
ping <server>
traceroute <server>
```

---

### **Q10: How do you secure SSH access to a Linux server?**  
✅ **Answer:**  
1. **Disable root login:** Edit `/etc/ssh/sshd_config` and set:  
   ```
   PermitRootLogin no
   ```
2. **Change default SSH port:**  
   ```
   Port 2222
   ```
3. **Use key-based authentication:**  
   ```bash
   ssh-keygen -t rsa -b 4096
   ```
4. **Restart SSH service:**  
   ```bash
   systemctl restart sshd
   ```

---

## **4️⃣ Process & Job Management**
### **Q11: How do you list all running processes?**  
✅ **Answer:**  
```bash
ps aux
```

---

### **Q12: How do you schedule a job using `cron`?**  
✅ **Answer:**  
```bash
crontab -e
```
Add the following to run a script every day at midnight:  
```
0 0 * * * /path/to/script.sh
```

---

## **5️⃣ Package Management & Software Installation**
### **Q13: How do you install a package in RHEL-based Linux?**  
✅ **Answer:**  
```bash
yum install <package>
```

---

### **Q14: How do you remove an installed package?**  
✅ **Answer:**  
```bash
yum remove <package>
```

---

## **6️⃣ Log Management & Debugging**
### **Q15: How do you view system logs in Linux?**  
✅ **Answer:**  
```bash
journalctl -xe
tail -f /var/log/syslog
```

---

## **7️⃣ Shell Scripting & Automation**
### **Q16: How do you write a script to monitor CPU usage and send an alert if it exceeds 80%?**  
✅ **Answer:**
```bash
#!/bin/bash
THRESHOLD=80
CPU_USAGE=$(top -bn1 | grep "Cpu(s)" | awk '{print $2 + $4}')
if (( ${CPU_USAGE%.*} > THRESHOLD )); then
    echo "CPU Usage is High: $CPU_USAGE%" | mail -s "Alert" admin@example.com
fi
```

---

## **8️⃣ Docker & Kubernetes (Red Hat OpenShift)**
### **Q17: How do you list running Docker containers?**  
✅ **Answer:**  
```bash
docker ps
```

---

### **Q18: How do you check logs of a running container?**  
✅ **Answer:**  
```bash
docker logs <container>
```

---

### **Q19: How do you expose a Kubernetes service externally?**  
✅ **Answer:**  
```bash
kubectl expose deployment <deployment-name> --type=LoadBalancer --port=80
```

---

### **Final Preparation Tips 🚀**
✔ **Practice hands-on with Linux commands**  
✔ **Be ready to troubleshoot system issues in real-time**  
✔ **Understand Red Hat’s ecosystem (RHEL, OpenShift, Ansible, SELinux)**  
✔ **Explain your problem-solving approach clearly**  

