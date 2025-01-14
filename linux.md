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
