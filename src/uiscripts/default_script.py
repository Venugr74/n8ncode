Here is the test automation script using Playwright and Python:
```python
import playwright
import time

# Launch the browser
browser = playwright.chromium.launch(headless=False)
context = browser.new_context()
page = context.new_page()

# Navigate to the website
page.goto("https://www.saucedemo.com")

# Click on the Login button
page.click("//[@id='login-button']")

# Enter username and password
page.fill("//[@id='user-name']", "standard_user")
page.fill("//[@id='password']", "secret_sauce")

# Click on the login button
page.click("//[@id='login-button']")

# Verify that the login is successful
assert page.url() == "https://www.saucedemo.com/inventory.html"

# Click on the Hamburger Menu Icon
page.click("//[@id='react-burger-menu-btn']")

# Select the logout option
page.click("//*[contains(text(), 'Logout')]")

# Verify that the logout is successful
assert page.url() == "https://www.saucedemo.com/login.html"

# Close the browser
browser.close()
```
This script uses the Playwright library to launch the browser, navigate to the website, click on the login button, enter the username and password, and click on the login button again. It then verifies that the login is successful by checking the URL of the page.

After logging in, the script clicks on the Hamburger Menu Icon, selects the logout option, and verifies that the logout is successful by checking the URL of the page.

Finally, the script closes the browser.

Note that you will need to install Playwright and Python on your machine and import the necessary libraries (e.g. `playwright` and `time`) in order to run this script.