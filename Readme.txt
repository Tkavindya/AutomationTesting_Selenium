Selenium Automation Testing - Login Script

---

Overview:

This project demonstrates automation testing of the login functionality for the Parabank web application using Selenium WebDriver in Python. The script validates login attempts with both valid and invalid credentials and saves screenshots of the results.

---

Features:

- Automates the login process for the Parabank application.
- Tests two scenarios: successful login and failed login.
- Saves screenshots for both scenarios in an `images` directory.

---

Prerequisites:

1. Python:
   - Download and install Python from [Python.org](https://www.python.org/downloads/).
   - During installation, check the box to "Add Python to PATH".
   - Verify installation:
     ```bash
     python --version
     ```

2. Selenium:
   - Install Selenium using pip:
     ```bash
     pip install selenium
     ```

3. ChromeDriver:
   - Download ChromeDriver from [ChromeDriver Downloads](https://sites.google.com/chromium.org/driver/).
   - Ensure the version matches your installed Chrome browser version.
   - Extract the downloaded file and note the `chromedriver.exe` path.

4. Environment Variables (Optional but Recommended):
   - Add the ChromeDriver path to your system environment variables:
     1. Search for "Edit the system environment variables" on your computer.
     2. Open Environment Variables.
     3. Under `System Variables`, find and edit the `Path` variable.
     4. Add the path to your ChromeDriver (e.g., `C:\path\to\chromedriver`).

5. Browser:
   - Install the Chrome browser (latest stable version).

---

Setup Instructions:


1. Run the Script:
   - Open a terminal or command prompt.
   - Navigate to the project directory:
     ```bash
     cd path\to\project
     ```
   - Execute the script:
     ```bash
     python test_login.py
     ```

2. Screenshots:
   - Upon script execution:
     - A successful login screenshot will be saved as `images/login_successful.png`.
     - A failed login screenshot will be saved as `images/login_failed.png`.

---

Test Details:

- URL:  
  ```
  https://parabank.parasoft.com/parabank/index.htm
  ```

- Credentials:  
  - Valid: `john / demo`  
  - Invalid: `wronguser / wrongpassword`

---

Troubleshooting:

1. NoSuchElementException:
   - Ensure the website's structure or element locators (e.g., `name="username"`) haven't changed.
   - Update the script if needed by inspecting the website with Chrome Developer Tools.

2. ChromeDriver Version Mismatch:
   - Ensure the ChromeDriver version matches your Chrome browser version.

3. Permission Issues:
   - Run the terminal/command prompt as an administrator if required.

---