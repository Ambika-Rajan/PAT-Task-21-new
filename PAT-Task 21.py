from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set the path to your WebDriver
driver = webdriver.Chrome()

try:
    # Step 1: Navigate to the Sauce Demo website
    driver.get("https://www.saucedemo.com/")

    # Allow time for the page to load
    time.sleep(2)

    # Step 2: Get cookies before login
    cookies_before_login = driver.get_cookies()
    print("Cookies before login:", cookies_before_login)

    # Step 3: Perform the login
    username_input = driver.find_element(By.ID, 'user-name')
    password_input = driver.find_element(By.ID, 'password')
    login_button = driver.find_element(By.CLASS_NAME, 'btn_action')

    username_input.send_keys('standard_user')  # Replace with your username
    password_input.send_keys('secret_sauce')  # Replace with your password
    login_button.click()

    # Allow time for the dashboard to load
    time.sleep(5)

    # Step 4: Get cookies after login
    cookies_after_login = driver.get_cookies()
    print("Cookies after login:", cookies_after_login)

    # Step 5: Perform the logout
    menu_button = driver.find_element(By.ID, 'react-burger-menu-btn')
    menu_button.click()

    logout_button = driver.find_element(By.ID, 'logout_sidebar_link')
    logout_button.click()

    # Allow time for the logout to complete
    time.sleep(2)

    # Step 6: Get cookies after logout
    cookies_after_logout = driver.get_cookies()
    print("Cookies after logout:", cookies_after_logout)

finally:
    # Close the browser
    driver.quit()
