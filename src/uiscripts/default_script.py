Here is the test automation script using Playwright and Python:
```python
import playwright
import time

# Set up the browser and page
browser = playwright.chromium.launch()
page = browser.new_page()

# Navigate to the website
page.goto("https://www.saucedemo.com")

# Click on the Login button
page.click("//[@id='login-button']")

# Enter username and password
page.fill("//[@id='user-name']", "standard_user")
page.fill("//[@id='password']", "secret_sauce")

# Click the Login button
page.click("//[@id='login-button']")

# Verify that the login is successful
assert page.url() == "https://www.saucedemo.com/inventory.html"

# Click on the Hamburger Menu Icon
page.click("//[@id='react-burger-menu-btn']")

# Select the logout option
page.click("//*[id='logout_sidebar_link']")

# Verify that the logout is successful
assert page.url() == "https://www.saucedemo.com/login"

# Close the browser
browser.close()
```
Let me explain what the script does:

1. It sets up the browser and page using Playwright.
2. It navigates to the website `https://www.saucedemo.com`.
3. It clicks on the Login button.
4. It enters the username `standard_user` and password `secret_sauce` using the `fill` method.
5. It clicks the Login button again to submit the credentials.
6. It verifies that the login is successful by checking the URL of the page.
7. It clicks on the Hamburger Menu Icon.
8. It selects the logout option by clicking on the `logout_sidebar_link` element.
9. It verifies that the logout is successful by checking the URL of the page.
10. Finally, it closes the browser.

Note that this script uses the `playwright` library to interact with the browser and perform the test steps. The `page` object is used to navigate to the website, fill in the username and password, click on elements, and verify the URLs. The `assert` statement is used to verify that the login and logout are successful.