# Module to request credentials from user and store as variables

import sys
import getpass

# Username Input
username = input("Please provide the ssh username: ")
if not username:
    print(f"Username not provided. Exiting script")
    sys.exit()
else:
    print(f"Username: {username}")

# Password Input
password = getpass.getpass(prompt="Please provide the ssh password: ")
if not password:
    print(f"SSH Password not provided. Exiting script")
    sys.exit()
else:
    print(f"SSH Password: ***************")

# Enable Password Input
enable_pass = getpass.getpass(prompt="Please provide the enable password (Leave blank if none needed): ")
if not enable_pass:
    print(f"Enable Password: None Provided")
else:
    print(f"Enable Password: ***************")