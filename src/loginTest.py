Below is a sample test automation script using Playwright and Python that accomplishes the specified steps for the `loginTest.py` file. Make sure you have Playwright installed in your Python environment. If you haven't done so already, you can install it using pip:

```bash
pip install playwright
python -m playwright install
```

Here is the test script:

```python
# loginTest.py
import asyncio
from playwright.async_api import async_playwright

async def run(playwright):
    # Launch the browser
    browser = await playwright.chromium.launch(headless=False)  # Set headless=True to run without a UI
    context = await browser.new_context()
    page = await context.new_page()

    # Step 1: Open website
    await page.goto("https://www.saucedemo.com")

    # Step 2: Enter username and password, then login
    await page.fill('//*[@id="user-name"]', 'standard_user')  # Entering username
    await page.fill('//*[@id="password"]', 'secret_sauce')    # Entering password
    await page.click('//*[@id="login-button"]')               # Click on the login button

    # Step 3: Click on the Hamburger Menu Icon and select logout
    await page.click('//*[@id="react-burger-menu-btn"]')      # Click Hamburger menu
    await page.click('//*[@id="logout_sidebar_link"]')         # Click Logout option

    # Closing the browser
    await browser.close()

# This is the entry point for the async function
async def main():
    async with async_playwright() as playwright:
        await run(playwright)

# Running the main function
if __name__ == "__main__":
    asyncio.run(main())
```

### Explanation of the Code:
1. **Imports**: The script imports necessary modules from `playwright.async_api` to work with asynchronous functions.
2. **Function to Run the Test**: The `run` function contains the test steps:
   - Navigates to the Sauce Demo website.
   - Fills in the username and password from the provided XPaths.
   - Clicks the login button.
   - After logging in, it clicks the hamburger menu icon and selects the logout option.
3. **Browser Context**: The browser context is created, and a new page is opened for the test.
4. **Main Function**: The `main` function manages the Playwright context and invokes the `run` function.
5. **Execution**: The script is executed in an asyncio event loop.

### Notes:
- If you want to run this in a headless environment (without a graphical UI), you can set `headless=True` in the `launch` method.
- Make sure to handle exceptions and assertions as necessary for a more robust test environment, especially for larger test suites.