Here's a Playwright test automation script in Python that performs the specified test steps for logging into the website `https://www.saucedemo.com` and then logging out:

```python
# newloginTest.py

import asyncio
from playwright.async_api import async_playwright

async def run_playwright_test():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False) # Set to True to run in the background
        page = await browser.new_page()

        # Step 1: Open website
        await page.goto("https://www.saucedemo.com")

        # Step 2: Enter credentials and login
        await page.fill('//*[@id="user-name"]', "standard_user")
        await page.fill('//*[@id="password"]', "secret_sauce")
        await page.click('//*[@id="login-button"]')

        # Step 3: Log out
        await page.click('//button[@id="react-burger-menu-btn"]')  # Click on the Hamburger Menu Icon
        await page.click('text=Logout')  # Select the Logout option

        # Close the browser
        await browser.close()

# Execute the test
if __name__ == "__main__":
    asyncio.run(run_playwright_test())
```

### Explanation of the Code:
1. **Import Playwright:** The script uses the `asyncio` and `playwright.async_api` modules for asynchronous test automation.
2. **Launch the Browser:** It launches a Chromium browser instance where `headless=False` allows you to see the browser UI.
3. **Navigate to the Site:** It opens `https://www.saucedemo.com`.
4. **Login:** It fills in the username and password fields using the provided XPaths and clicks the login button.
5. **Logout:** After successfully logging in, it clicks the Hamburger Menu Icon and selects the logout option.
6. **Close the Browser:** Finally, it closes the browser session.

### Usage:
- Ensure you have `Playwright` installed and set up in your Python environment. You can install it via pip:
  ```
  pip install playwright
  playwright install
  ```
- Save the above script as `newloginTest.py` and run it using:
  ```
  python newloginTest.py
  ```

This script will execute the steps you've detailed, testing the login and logout functionality of the Sauce Demo web application.