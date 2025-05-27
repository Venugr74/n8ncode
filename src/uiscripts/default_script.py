Here is the `loginTest.py` script using Playwright and Python:
```python
import pytest
from playwright.sync_api import sync_playwright

@pytest.mark.parametrize("username, password", [("standard_user", "secret_sauce")])
def test_login(playwright, username, password):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # Open the website
    page.goto("https://www.saucedemo.com")

    # Click on the Login button
    page.click("//button[@id='login-button']")

    # Enter username and password
    page.fill("//input[@id='user-name']", username)
    page.fill("//input[@id='password']", password)

    # Click the Login button
    page.click("//button[@id='login-button']")

    # Verify login successful
    assert page.url() == "https://www.saucedemo.com/inventory.html"

    # Click on the Hamburger Menu Icon
    page.click("//button[@id='react-burger-menu-btn']")

    # Select the logout option
    page.click("//*[contains(text(), 'Logout')]")

    # Verify logout successful
    assert page.url() == "https://www.saucedemo.com/"

    # Close the browser
    browser.close()
```
This script uses the `pytest` framework and the `playwright` library to launch a Chromium browser, navigate to the website, click on the login button, enter the username and password, and verify that the login is successful.

It then clicks on the hamburger menu icon, selects the logout option, and verifies that the logout is successful.

The script uses parameterized testing to run the test with the same credentials for all iterations.

Please note that this script is just a starting point and you may need to modify it to fit your specific testing needs.

Also, you need to have pytest and playwright installed in your environment, you can install them by running `pip install pytest playwright` command.

Please let me know if you have any questions or need further assistance.