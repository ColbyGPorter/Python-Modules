import pathlib
from pathlib import Path
import logging
import datetime
from datetime import datetime
import pythonping
from pythonping import ping

IpList = ['1.1.1.1', '10.10.10.10']

# Directory
log_dir = Path(r"C:\Filepath")
# Today's Date
today = datetime.now().strftime("%Y-%m-%d")
# Log file name and path (Creates file if not already there)
log_file = log_dir / f"Test_{today}.txt"
# Complete File Path
file_path = log_dir / log_file
# Timestamp for log message
timestamp = datetime.now().strftime("%H:%M:%S")

# # Testing Block
# print(f"Created: {file_path}")
# output = "Test Output"
# log_line = f"{timestamp} | {output}\n"
# with log_file.open("a", encoding="utf-8") as f:
#     f.write(log_line)

for DeviceIP in IpList:
    #Remove/Add verbose=True to hide/show all ping responses
    #Example --- response_list = ping(DeviceIP, count=5, verbose=True)
    response_list = ping(DeviceIP, count=5, timeout=1)
    if response_list.packet_loss > 0:
        loss_rate = response_list.packet_loss * 100
        loss_rate_str = str(loss_rate)
        # print(loss_rate_str)
        # Store desired message in variable
        output = DeviceIP + " is experiencing " + loss_rate_str + "% packet loss."
        print(output)
        # Create complete log line message for log file
        log_line = f"{timestamp} | {output}\n"
        # Opens log file, appends log message from stored variable
        with log_file.open("a", encoding="utf-8") as f:
            f.write(log_line)
        print("")
    else:
        # Store desired message in variable
        output = DeviceIP + " is online."
        print(output)
        # Create complete log line message for log file
        log_line = f"{timestamp} | {output}\n"
        # Opens log file, appends log message from stored variabl
        with log_file.open("a", encoding="utf-8") as f:
            f.write(log_line)
        print("")