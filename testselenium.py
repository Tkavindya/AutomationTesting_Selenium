from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize the browser
driver = webdriver.Chrome()
driver.get("https://parabank.parasoft.com/parabank/index.htm")  # URL

# Function to perform login and validate
def login_test(username, password):
    try:
        # Reset the page before each test case
        driver.get("https://parabank.parasoft.com/parabank/index.htm")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "username")))

        # Locate and fill the username field
        username_field = driver.find_element(By.NAME, "username")
        username_field.clear()
        for char in username:
            username_field.send_keys(char)
            time.sleep(0.1)  # Pause between keystrokes

        # Locate and fill the password field
        password_field = driver.find_element(By.NAME, "password")
        password_field.clear()
        for char in password:
            password_field.send_keys(char)
            time.sleep(0.1)  # Pause between keystrokes

        # Locate the login button and click
        login_button = driver.find_element(By.XPATH, "//input[@type='submit' and @value='Log In']")
        time.sleep(1)  # Pause before clicking the button
        login_button.click()

        # Validate the login status
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//h1[contains(text(), 'Accounts Overview')]"))
            )
            print("Login Successful")
            driver.save_screenshot("images/login_successful.png")
        except:
            print("Login Failed")
            driver.save_screenshot("images/login_failed.png")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        time.sleep(2)  # Give time before resetting the page

# Test cases
login_test("john", "demo")  # Valid credentials
login_test("wronguser", "wrongpassword")  # Invalid credentials

# Close the browser
driver.quit()
