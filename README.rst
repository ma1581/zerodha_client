ZerodhaClient
=============

ZerodhaClient is a Python package designed to automate the login process
and scrape dashboard details from Zerodha Coin using Playwright. This
package is intended for personal use to fetch investment details
programmatically.

Features
--------

-  Automates login to Zerodha Coin using Playwright.
-  Supports TOTP-based two-factor authentication.
-  Fetches investment details from the dashboard.

Installation
------------

Ensure you have Python installed (Python 3.7+ recommended). Install the
required dependencies before using the package:

::

   pip install playwright pyotp

You also need to install Playwright’s browsers:

::

   playwright install

Usage
-----

Import and Initialize
~~~~~~~~~~~~~~~~~~~~~

::

   from zerodha_client.main import ZerodhaClient


   ## Provide your TOTP authentication URL, username, and password
   totp_auth_url = "otpauth://totp/YourAccount?secret=YOUR_SECRET"
   username = "your_user_id"
   password = "your_password"

   client = ZerodhaClient(totp_auth_url, username, password)

Login to Zerodha Coin

::

   client.login()

Fetch Dashboard Details

::


   dashboard_details = client.get_dashboard_details()
   print(dashboard_details)

Close the Session

::

   client.close()

Dependencies
------------

-  playwright: Used for browser automation.
-  pyotp: Generates TOTP-based OTPs for authentication.

Notes
-----

-  This package is intended for personal use only.
-  Using automated tools to access financial services may violate terms
   of service. Ensure compliance before use.

Disclaimer
----------

This tool is not affiliated with or endorsed by Zerodha. Use it
responsibly and at your own risk.

Reference
---------

-  Git: https://github.com/ma1581/zerodha_client
-  PyPi: https://pypi.org/project/zerodha-client