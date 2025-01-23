1. **`os`, `sys`, and `platform`**: Used for system-level scripting and cross-platform compatibility checks.
2. **`subprocess`**: For running shell commands or integrating system tools into scripts.
3. **`psutil`**: System monitoring dashboards or health checks.
4. **`re`**: Parsing logs or validating user inputs like emails.
5. **`scapy`**: Creating network penetration testing tools.
6. **`requests`/`urllib3`**: API integration for web services.
7. **`logging`**: Error tracking in production environments.
8. **`boto3`**: Automating cloud resources in AWS.
9. **`paramiko`**: Remote server management tools.
10. **`json` and `PyYAML`**: Configuration-driven applications.

### **1. `os` Module**
- **Purpose**: Provides a way to interact with the operating system, such as file manipulation, directory management, environment variables, and process management.
- **Use Case**: Automating file and directory operations.
- **Example**:
  ```python
  import os

  # List all files in the current directory
  print(os.listdir("."))
  
  # Get the current working directory
  print(os.getcwd())

  # Create a new directory
  os.mkdir("new_folder")
  ```

---

### **2. `platform` Module**
- **Purpose**: Provides information about the underlying platform, such as OS, processor, and Python version.
- **Use Case**: Checking the OS to execute OS-specific commands.
- **Example**:
  ```python
  import platform

  # Get the OS name
  print(platform.system())  # Output: 'Linux', 'Windows', etc.

  # Get processor details
  print(platform.processor())

  # Get Python version
  print(platform.python_version())
  ```

---

### **3. `subprocess` Module**
- **Purpose**: Allows you to run system commands and interact with them programmatically.
- **Use Case**: Automating tasks that require shell commands (e.g., running a script or checking system status).
- **Example**:
  ```python
  import subprocess

  # Run a shell command and get the output
  result = subprocess.run(["ls", "-l"], capture_output=True, text=True)
  print(result.stdout)
  ```

---

### **4. `sys` Module**
- **Purpose**: Provides access to system-specific parameters and functions, such as command-line arguments and exiting the program.
- **Use Case**: Handling command-line arguments in scripts.
- **Example**:
  ```python
  import sys

  # Access command-line arguments
  print(sys.argv)

  # Exit the program
  sys.exit("Exiting program")
  ```

---

### **5. `psutil` Module**
- **Purpose**: Provides information about system processes and resource usage (CPU, memory, disks, etc.).
- **Use Case**: Monitoring system health.
- **Example**:
  ```python
  import psutil

  # Get CPU usage
  print(psutil.cpu_percent(interval=1))

  # Get memory usage
  print(psutil.virtual_memory())
  ```

---

### **6. `re` Module (Regular Expression)**
- **Purpose**: Provides support for working with regular expressions for pattern matching in strings.
- **Use Case**: Validating email addresses or extracting data from text.
- **Example**:
  ```python
  import re

  # Validate an email address
  email = "test@example.com"
  if re.match(r"[^@]+@[^@]+\.[^@]+", email):
      print("Valid email")
  ```

---

### **7. `scapy` Module**
- **Purpose**: A library for network packet manipulation and analysis.
- **Use Case**: Crafting custom packets or sniffing network traffic.
- **Example**:
  ```python
  from scapy.all import *

  # Sniff packets
  sniff(prn=lambda x: x.summary(), count=10)
  ```

---

### **8. `requests` and `urllib3` Modules**
- **Purpose**:
  - `requests`: Simplifies making HTTP requests.
  - `urllib3`: A low-level HTTP client for advanced control.
- **Use Case**: Making API calls.
- **Example** (Using `requests`):
  ```python
  import requests

  response = requests.get("https://jsonplaceholder.typicode.com/posts")
  print(response.json())
  ```

---

### **9. `logging` Module**
- **Purpose**: Provides a way to log messages for debugging and monitoring.
- **Use Case**: Tracking application flow and errors.
- **Example**:
  ```python
  import logging

  logging.basicConfig(level=logging.INFO)
  logging.info("This is an info message")
  logging.error("This is an error message")
  ```

---

### **10. `getpass` Module**
- **Purpose**: Allows for securely capturing passwords without echoing them to the console.
- **Use Case**: Prompting for credentials in CLI tools.
- **Example**:
  ```python
  import getpass

  password = getpass.getpass("Enter your password: ")
  print("Password entered:", password)
  ```

---

### **11. `boto3` Module**
- **Purpose**: The AWS SDK for Python to interact with AWS services.
- **Use Case**: Managing S3 buckets or launching EC2 instances.
- **Example**:
  ```python
  import boto3

  s3 = boto3.client("s3")
  for bucket in s3.list_buckets()["Buckets"]:
      print(bucket["Name"])
  ```

---

### **12. `paramiko` Module**
- **Purpose**: Used for SSH and SFTP communication.
- **Use Case**: Automating tasks on remote servers.
- **Example**:
  ```python
  import paramiko

  ssh = paramiko.SSHClient()
  ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
  ssh.connect("hostname", username="user", password="password")

  stdin, stdout, stderr = ssh.exec_command("ls -l")
  print(stdout.read().decode())
  ssh.close()
  ```

---

### **13. `json` Module**
- **Purpose**: Handles JSON data (parsing and serialization).
- **Use Case**: Reading or writing JSON configuration files.
- **Example**:
  ```python
  import json

  data = {"name": "Alice", "age": 30}
  json_data = json.dumps(data)  # Convert to JSON string
  print(json.loads(json_data))  # Convert JSON string back to Python dictionary
  ```

---

### **14. `PyYAML` Module**
- **Purpose**: Provides support for parsing and writing YAML files.
- **Use Case**: Reading configuration files.
- **Example**:
  ```python
  import yaml

  yaml_data = """
  name: Alice
  age: 30
  """
  data = yaml.safe_load(yaml_data)
  print(data)
  ```

---
