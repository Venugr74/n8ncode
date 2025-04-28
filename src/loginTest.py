Below is a complete Playwright test automation script named **`loginTest.py`**. The script performs the login and logout functionalities on the Sauce Demo website according to the provided steps and XPaths.

```python
# loginTest.py

import asyncio
from playwright.async_api import async_playwright

async def run(playwright):
    # Launch an instance of the browser
    browser = await playwright.chromium.launch(headless=False)  # Set to True for headless mode
    context = await browser.new_context()
    page = await context.new_page()

    try:
        # Step 1: Navigate to the Sauce Demo website
        await page.goto("https://www.saucedemo.com")

        # Step 2: Enter username and password
        await page.fill('//*[@id="user-name"]', 'standard_user')  # Enter username
        await page.fill('//*[@id="password"]', 'secret_sauce')   # Enter password

        # Step 3: Click the login button
        await page.click('//*[@id="login-button"]')

        # Wait for navigation to complete after logging in
        await page.wait_for_navigation()
        
        # Step 4: Click on the Hamburger Menu Icon
        await page.click('//*[@id="react-burger-menu-btn"]')

        # Step 5: Select the logout option
        await page.click('//*[@id="logout_sidebar_link"]')

        # Optionally wait for a moment to observe the effect of logout
        await page.wait_for_timeout(3000)

    finally:
        # Close the browser context and the browser
        await context.close()
        await browser.close()

# Execute the script
if __name__ == "__main__":
    asyncio.run(run(async_playwright()))
```

### Explanation of the Code:
1. **Imports**: 
   - The necessary modules from `playwright.async_api` are imported for asynchronous handling of browser actions.
  
2. **`run` Function**:
   - This function encapsulates all our automation logic:
     - It launches a Chromium browser in non-headless mode (for debugging).
     - It navigates to the Sauce Demo website and inputs credentials (`standard_user` and `secret_sauce`).
     - It clicks the login button and waits for the page to load.
     - It accesses the hamburger menu and selects the logout option.
  
3. **Error Handling**: 
   - The use of `try...finally` ensures that the browser is closed even if an error occurs during execution.

4. **Execution**: 
   - The script is designed to be run directly. It uses `asyncio.run()` to handle asynchronous operations.

### Prerequisites:
- Install Playwright if you haven’t already:
  ```bash
  pip install playwright
  playwright install
  ```

### Notes:
- The line `headless=False` allows you to see the browser actions; change it to `True` when you want to run the test in headless mode.
- The script is kept simple and straightforward for clarity. You may enhance it further by adding assertions or logging as needed.