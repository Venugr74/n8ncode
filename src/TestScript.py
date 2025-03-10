 Here's an example of how you can write an automated UI test using Python and Playwright to verify the functionality of a web application as per your requirements. I've created a file named `TestScript.py` in the directory `src`.

```python
# src/TestScript.py

import time
from playwright.async_api import Playwright, async_playwright
from pages.login_page import LoginPage

async def test_forecast_explorer_ui(playwright):
    browser = await playwright.chromium.launch(headless=False)
    context = await browser.newContext()
    page = await context.newPage()

    # Login to the website
    login_page = LoginPage(page)
    await login_page.login()

    # Navigate to Feature Store
    await page.waitForSelector('span.sc-irPVuy.fYDalG').click()
    await page.waitForSelector('//span[normalize-space()="Feature Store"]').click()

    # Wait for "Launch Feature Job" button to visible
    await page.waitForSelector('(//button[normalize-space()="Launch Feature Job"])[1]')

    # Click on "Launch Feature Job" Button
    launch_feature_job_btn = await page.querySelector('(//button[normalize-space()="Launch Feature Job"])[1]')
    await launch_feature_job_btn.click()

    # Wait for "Job Selector" button to visible
    await page.waitForSelector(JobSelector)

    # Verify the "Job Selector" button is visible
    job_selector = await page.querySelector(JobSelector)
    assert job_selector is not None, "Job Selector button is not visible."

    # Close the browser
    await browser.close()

async def main():
    playwright = await async_playwright.create()
    try:
        result = await test_forecast_explorer_ui(playwright)
        print("Test executed successfully.")
    except Exception as e:
        print("Test execution failed with error:", str(e))
    finally:
        await playwright.stop()

if __name__ == "__main__":
    main()
```

This test script does the following:
- Launches a non-headless browser using Chromium
- Logs in to the website using the `login_page` class from `pages.login_page` and the `login` method
- Navigates to the Feature Store
- Waits for the "Launch Feature Job" button and clicks it
- Waits for the "Job Selector" button and verifies that it's visible by checking if it's not None
- Closes the browser when done

Make sure to replace `JobSelector` with your actual job selector value.

You should also create a folder named `pages` where you define your pages, in this case, the `login_page`. Here's an example of how to implement the `LoginPage` class:

```python
# pages/login_page.py
from playwright.async_api import Page

class LoginPage:
    def __init__(self, page):
        self.page = page

    async def login(self):
        # Locate the username and password fields and login button using their selectors
        await self.page.waitForSelector('//input[@name="username"]')
        await self.page.waitForSelector('//input[@name="password"]')
        await self.page.waitForSelector('//button[normalize-space()="Login"]')

        # Fill in the username and password fields
        await self.page.fill('//input[@name="username"]', 'your_username')
        await self.page.fill('//input[@name="password"]', 'your_password')

        # Click on the login button
        await self.page.click('//button[normalize-space()="Login"]')
```