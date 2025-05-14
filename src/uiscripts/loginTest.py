Below is a production-quality test automation script named `loginTest.py` that uses Playwright with Python to perform the login and logout actions on the specified website using the provided XPaths.

```python
import asyncio
from playwright.async_api import async_playwright

async def run_test():
    async with async_playwright() as p:
        # Launch browser
        browser = await p.chromium.launch(headless=False)  # Change to True for headless mode
        page = await browser.new_page()

        # Step 1: Open website
        await page.goto("https://www.saucedemo.com")

        # Step 2: Login
        await page.fill('//*[@id="user-name"]', 'standard_user')
        await page.fill('//*[@id="password"]', 'secret_sauce')
        await page.click('//*[@id="login-button"]')

        # Step 3: Verify login success by checking the URL or a specific element
        await page.wait_for_selector('//*[@id="react-burger-menu-btn"]', timeout=5000)

        # Step 4: Access sidebar menu and logout
        await page.click('//*[@id="react-burger-menu-btn"]')  # Click on Hamburger Menu Icon
        await page.click('//*[@id="logout_sidebar_link"]')  # Click on Logout option

        # Step 5: Verify logout by ensuring the login button is visible again
        await page.wait_for_selector('//*[@id="login-button"]', timeout=5000)

        # Close the browser
        await browser.close()

if __name__ == "__main__":
    asyncio.run(run_test())
```

### Explanation:
- **Imports**: The script begins by importing necessary libraries from the `playwright.async_api`.
- **Asynchronous Execution**: The test is executed asynchronously to improve performance, especially with web automation tasks.
- **Browser Launch**: The script launches a Chromium browser instance, with the option to run headless (without UI).
- **Navigating to the website**: The script navigates to `https://www.saucedemo.com`.
- **Filling in Credentials**: The script fills in the username and password using the specified XPaths.
- **Login Success Verification**: After submitting the login form, the script waits for a specific element (`Hamburger Menu Icon`) to ensure that the login was successful.
- **Logging Out**: The script proceeds to click on the hamburger menu and then on the logout option.
- **Logout Verification**: It checks if the login button is visible again to confirm that the logout was successful.
- **Cleanup**: Finally, it closes the browser to free up resources.

### Running the Script:
To run this script, ensure you have Playwright installed in your Python environment. You can install it using pip:

```sh
pip install playwright
playwright install  # Install browser binaries
```

After setting up, execute the script:
```sh
python loginTest.py
```

Make sure to adjust the `headless` parameter as per your preference.