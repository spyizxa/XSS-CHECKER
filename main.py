from time import sleep
import os
import sys
import requests

RESET = "\033[0m"
HEADER = "\033[95m"
OKGREEN = "\033[92m"
WARNING = "\033[93m"
FAIL = "\033[91m"

print(f"""{HEADER}
__  ______ ____     ____ _   _ _____ ____ _  _______ ____
\ \/ / ___/ ___|   / ___| | | | ____/ ___| |/ / ____|  _ \\
 \  /\___ \___ \  | |   | |_| |  _|| |   | ' /|  _| | |_) |
 /  \ ___) |__) | | |___|  _  | |__| |___| . \| |___|  _ <
/_/\_\____/____/   \____|_| |_|_____\____|_|\_\_____|_| \_\\
{RESET}

{OKGREEN}XSS CHECKER V1.0 | TELEGRAM: @zero_exploits{RESET}

{WARNING}xss checker checks whether the target has xss vulnerabilities!{RESET}

use:
    python3 main.py   
""")

url = input("Target URL: ")

try:
    with open('payloadlist.txt', 'r') as file:
        payloads = [line.strip() for line in file.readlines()]
except FileNotFoundError:
    print(f"{FAIL}Error: payloadlist.txt not found!{RESET}")
    sys.exit(1)

while True:
    for payload in payloads:
        params = {'q': payload}
        try:
            response = requests.get(url, params=params)
            if response.status_code == 200:
                if payload in response.text:
                    print(f"{OKGREEN}XSS vulnerable with payload: {payload}{RESET}")
                    user_input = input("Should I exit the program? (y/n): ").lower()
                    if user_input == "y":
                        sys.exit(0)
                else:
                    print(f"{FAIL}XSS not vulnerable with payload: {payload}{RESET}")
            else:
                print(f"{FAIL}Server returned status code: {response.status_code}{RESET}")
        except requests.exceptions.RequestException as e:
            print(f"{FAIL}An error occurred: {e}{RESET}")
            sleep(3)
            print("Logging out!")
            sys.exit(0)

        sleep(1)

    print("Restarting the payload check...")
    sleep(2)