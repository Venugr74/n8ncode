Certainly! Below is a Python script called `loginTest.py` using Playwright for automating the login process for the specified website, followed by logging out. Make sure you have Playwright installed in your Python environment before running the script.

```python
# loginTest.py

import asyncio
from playwright.async_api import async_playwright


async def run(playwright):
    # Start the browser
    browser = await playwright.chromium.launch(headless=False)
    context = await browser.new_context()
    page = await context.new_page()

    try:
        # Open the website
        await page.goto("https://www.saucedemo.com")

        # Enter username
        await page.fill('//*[@id="user-name"]', 'standard_user')

        # Enter password
        await page.fill('//*[@id="password"]', 'secret_sauce')

        # Click on the login button
        await page.click('//*[@id="login-button"]')

        # Wait for navigation after login
        await page.wait_for_navigation()

        # Click on the Hamburger Menu Icon
        await page.click('//*[@id="react-burger-menu-btn"]')
        
        # Click on the logout option
        await page.click('//*[@id="logout_sidebar_link"]')

        # Wait for navigation after logout
        await page.wait_for_navigation()

        print("Logged out successfully!")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Close the browser
        await browser.close()


async def main():
    async with async_playwright() as playwright:
        await run(playwright)


if __name__ == "__main__":
    asyncio.run(main())
```

### Explanation:
1. **Imports**: The script imports necessary modules from the Playwright library.
2. **Browser Setup**: The browser launches in a non-headless mode (`headless=False`) to visualize the actions.
3. **Navigation**: The page navigates to `https://www.saucedemo.com`.
4. **Actions**:
   - It fills in the username and password fields using the specified XPaths.
   - It clicks the login button and waits for the navigation to occur post-login.
   - After successful login, it clicks the hamburger menu and navigates to the logout option.
5. **Error Handling**: It includes a try-except block to catch any exceptions and print errors for better debugging.
6. **Cleanup**: The browser closes after the operations complete.

### Prerequisites:
Ensure you have the Playwright library installed. You can do this via pip:
```bash
pip install playwright
playwright install
```

### Running the Test:
To run the test, simply execute the script using Python:
```bash
python loginTest.py
```

This will perform the automated login and logout sequence as described.