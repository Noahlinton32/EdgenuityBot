Edgenuity Automation with Selenium
Overview

This Python script uses Selenium to automate the login and navigation process for the Edgenuity platform. It automates the login, navigates to specific sections, and performs actions on the platform.
Prerequisites

    Python 3.x
    Selenium
    Firefox browser
    geckodriver

Installation

    Install Python from python.org
    Install Selenium:

    pip install selenium

    Download Firefox browser from firefox.com
    Download geckodriver from geckodriver

Setup

    Clone or download the repository.
    Place the geckodriver.exe in the specified directory: C:\Users\Noah Linton\Downloads\New folder\.
    Update the username and password variables in the script with your Edgenuity credentials.

Execution

Run the script using the following command:

bash

python edgenuity_automation.py

Important Notes

    The script uses time.sleep() as a buffer to prevent the program from clicking on an element that doesn't exist immediately after loading.
    Ensure you have a stable internet connection when running the script.
    Adjust the sleep times as needed based on your network speed and system performance.

Disclaimer

This script is for educational purposes only. Use it responsibly and at your own risk. Avoid excessive use to prevent potential restrictions or account bans.
