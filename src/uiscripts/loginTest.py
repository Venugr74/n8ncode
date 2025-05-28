Here is a sample test automation script using Playwright and Python named `loginTest.py`:
```python
import playwright
from playwright.sync_api import sync_playwright

# Set up playwright
with sync_playwright() as p:
    browser = p.chromium.launch()
    context = browser.new_context()
    page = context.new_page()

    # Navigate to the website
    page.goto("https://www.saucedemo.com")

    # Click on the Login button
    page.click("//[@id='login-button']")

    # Enter username and password
    page.fill("//[@id='user-name']", "standard_user")
    page.fill("//[@id='password']", "secret_sauce")

    # Click the login button
    page.click("//[@id='login-button']")

    # Verify login is successful
    assert page.url() == "https://www.saucedemo.com/inventory.html"

    # Click on the Hamburger Menu Icon
    page.click("//[@id='react-burger-menu-btn']")

    # Select the logout option
    page.click("//[@id='logout_sidebar_link']")

    # Verify logout is successful
    assert page.url() == "https://www.saucedemo.com/login.jsp"

    # Clean up
    browser.close()
```
This script uses the `playwright` library to launch a Chromium browser, navigate to the website, click on the Login button, enter the username and password, click the login button, verify the login is successful, click on the Hamburger Menu Icon, select the logout option, and verify the logout is successful.

Note that this script assumes that the website uses the same login credentials and logout functionality as the example provided. You may need to modify the script to suit your specific use case.

Also, this script uses the `sync_playwright` API, which is synchronous. If you prefer to use the asynchronous API, you can use the `async` keyword and the `await` keyword instead of the `sync` API.

You can run this script using the following command:
```
python loginTest.py
```
Make sure to install the `playwright` library by running the following command:
```
pip install playwright
```
Before running the script, make sure to have a stable internet connection and that the website is available.