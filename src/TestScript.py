 Here's an example of how you can create the `TestScript.py` file with the given requirements using Python and Playwright:

```python
# src/TestScript.py

from playwright.async_api import Playwright, async_playwright
import time
from pages.login_page import LoginPage

async def test_forecast_explorer_ui(browser):
    # Navigate to the Feature Store page
    await browser.new_tab(name="Feature Store")
    await browser.goto("https://your-webapp-url.com")

    # Login using LoginPage class and login method
    login_page = LoginPage(browser)
    await login_page.login()

    # Click the Feature Store Icon
    feature_store_icon = await browser.query_selector("span.sc-irPVuy.fYDalG")
    await feature_store_icon.click()

    # Click the Feature Store Text
    await browser.wait_for_selector("//span[normalize-space()='Feature Store']").click()

    # Wait for Launch Feature Job button to be visible
    launch_feature_job_button = await browser.query_selector("(//button[normalize-space()="Launch Feature Job"])[1]")
    await launch_feature_job_button.wait_for({'visible': True})

    # Click on Launch Feature Job Button
    await launch_feature_job_button.click()

    # Wait for Job Selector button to be visible
    job_selector = await browser.query_selector("button.sc-blHHSb.dxiEPq")
    await job_selector.wait_for({'visible': True})

    # Verify the Job Selector button is visible
    assert job_selector.is_visible()

async def main():
    browser = await async_playwright().start(headless=False)
    context = await browser.new_context()
    page = await context.new_page()

    try:
        await test_forecast_explorer_ui(page)
    finally:
        await context.close()
        await browser.close()

if __name__ == "__main__":
    main()
```

Please note that this is a basic example, and you should modify it according to your specific application URL, login details, and any potential exceptions during the test execution. Also, make sure to have Playwright installed:

```sh
pip install playwright
```

For the `pages/login_page.py`, you can create a separate file containing the LoginPage class as follows:

```python
# pages/login_page.py

from playwright.async_api import Page

class LoginPage:
    def __init__(self, page):
        self.page = page

    async def login():
        # Implement your login functionality here
        await self.page.fill('username_field', 'your-username')
        await self.page.fill('password_field', 'your-password')
        await self.page.click('login_button')
```