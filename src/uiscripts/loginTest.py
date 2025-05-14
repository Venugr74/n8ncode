Here's a Playwright test automation script written in Python named `loginTest.py`. This script follows the given test steps and XPath locators to perform the login and logout actions on the specified website (`https://www.saucedemo.com`).

Make sure you have Playwright installed in your Python environment. If you haven't installed it yet, you can do so using pip:

```bash
pip install playwright
```

After installing Playwright, you also need to install the necessary browsers:

```bash
playwright install
```

Now, here's the `loginTest.py` script:

```python
from playwright.sync_api import sync_playwright

def run(playwright):
    # Launch the browser
    browser = playwright.chromium.launch(headless=False)  # Set headless=True to run without a UI
    context = browser.new_context()
    page = context.new_page()
    
    # Navigate to the website
    page.goto("https://www.saucedemo.com")
    
    # Enter username
    page.fill('//*[@id="user-name"]', "standard_user")
    
    # Enter password
    page.fill('//*[@id="password"]', "secret_sauce")
    
    # Click the Login button
    page.click('//*[@id="login-button"]')
    
    # Wait for navigation after login
    page.wait_for_navigation()
    
    # Click on the Hamburger Menu Icon
    page.click('//*[@id="react-burger-menu-btn"]')
    
    # Click on the logout option
    page.click('//*[@id="logout_sidebar_link"]')
    
    # Close the browser
    context.close()
    browser.close()

if __name__ == "__main__":
    with sync_playwright() as playwright:
        run(playwright)
```

### Explanation of the Script:
1. **Import Playwright**: We import `sync_playwright` from the `playwright.sync_api` module to interact with the browser.
2. **Launch the Browser**: A Chromium browser is launched. The `headless` parameter is set to `False` for visual observation; change it to `True` to run in headless mode.
3. **Navigate to the Website**: The script opens `https://www.saucedemo.com`.
4. **Fill in Credentials**: The script uses XPath locators to fill in the username and password fields.
5. **Click Login**: It clicks the login button and waits for navigation to complete.
6. **Logout Process**: It clicks on the Hamburger Menu and then clicks on the logout option.
7. **Close the Browser**: Finally, the context and browser are closed after the operations.

### Running the Script:
To execute the script, run the following command in your terminal:
```bash
python loginTest.py
```

Make sure your environment is set up correctly, and you'll see the script performing the login and logout actions on the website.