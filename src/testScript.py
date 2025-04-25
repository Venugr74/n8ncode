To automate the specified actions on the Sauce Demo website using Selenium in Python, you can create a script as outlined below. Make sure you have the Selenium package installed (`pip install selenium`) and the appropriate WebDriver for your browser (like ChromeDriver for Google Chrome).

Here’s a complete automation script based on your instructions:

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Setup the WebDriver (Make sure to specify the path to your WebDriver if necessary)
driver = webdriver.Chrome()

try:
    # Open Sauce Demo website
    driver.get("https://www.saucedemo.com")
    
    # Maximize the browser window
    driver.maximize_window()
    
    # Enter username
    username_field = driver.find_element(By.XPATH, '//*[@id="user-name"]')
    username_field.send_keys('standard_user')
    
    # Enter password
    password_field = driver.find_element(By.XPATH, '//*[@id="password"]')
    password_field.send_keys('secret_sauce')
    
    # Click on the login button
    login_button = driver.find_element(By.XPATH, '//*[@id="login-button"]')
    login_button.click()
    
    # Wait for the page to load
    time.sleep(2)

    # Click on the Hamburger Menu Icon
    hamburger_menu = driver.find_element(By.XPATH, '//*[@id="react-burger-menu-btn"]')
    hamburger_menu.click()
    
    # Select the logout option
    logout_button = driver.find_element(By.XPATH, '//*[@id="logout_sidebar_link"]')
    logout_button.click()
    
    # Wait for some time to observe the logout action
    time.sleep(2)

finally:
    # Close the browser
    driver.quit()
```

### Explanation:
1. **Import Libraries**: The script imports necessary modules from Selenium.
2. **WebDriver Setup**: It initializes a Chrome WebDriver (ensure you have the corresponding driver for the browser installed and correctly set up).
3. **Navigation and Login**: The script navigates to the Sauce Demo website, fills in the login form with the provided username and password, and submits the form.
4. **Logout Procedure**: After logging in, it accesses the hamburger menu and selects the logout option.
5. **Cleanup**: Finally, it closes the browser using `driver.quit()`.

### Notes:
- Implement `time.sleep()` to give the web page time to load between actions, but you might want to use WebDriver's built-in waits (`WebDriverWait`) for a more robust solution in real-world scenarios.
- Adjust the path to the `chromedriver` executable if necessary. If you're using Firefox or another browser, make sure to change the driver accordingly.