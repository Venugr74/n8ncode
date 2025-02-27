 Here is an example of how you can write the automated UI test using Python, Playwright, and the given details:

Firstly, create a folder named `src` if not already exists. Inside the `src` folder, create a new file named `TestScript.py`.

```python
# src/TestScript.py
from playwright.async_api import Playwright, async_playwright
import time
from pages.login_page import LoginPage

class ForecastExplorerUI:
    def __init__(self, browser):
        self.browser = browser

    async def test_forecast_explorer_ui(self):
        # Navigate to the Feature Store page
        await self.navigate_to_feature_store()

        # Wait for "Launch Feature Job" button to visible
        await self.wait_for_launch_feature_job_button()

        # Click on "Launch Feature Job" Button
        await self.click_launch_feature_job_button()

        # Wait for "Job Selector" button to visible
        await self.wait_for_job_selector_button()

        # Verify the "Job Selector" button is visible
        assert await self.is_visible(self.job_selector)

    async def navigate_to_feature_store(self):
        page = self.browser.new_page()
        await page.goto('http://your-website.com')

        # Login to website using LoginPage class and login method
        await LoginPage().login(page)

        # Click "Feature Store Icon"
        await page.locator('.fYDalG').click()

        # Click "Feature Store Text"
        await page.locator('//span[normalize-space()="Feature Store"]').click()

    async def wait_for_launch_feature_job_button(self):
        await self.browser.pause(2000)  # Adjust the waiting time as needed
        launch_button = self.browser.page().locator('(//button[normalize-space()="Launch Feature Job"])[1]')
        await launch_button.wait_for({'state': 'attached', 'visible': True})

    async def click_launch_feature_job_button(self):
        await self.browser.page().locator('(//button[normalize-space()="Launch Feature Job"])[1]').click()

    async def wait_for_job_selector_button(self):
        await self.browser.pause(2000)  # Adjust the waiting time as needed
        job_selector = self.browser.page().locator(self.job_selector)
        await job_selector.wait_for({'state': 'attached', 'visible': True})

    async def is_visible(self, locator):
        return await locator.isVisible()

    job_selector = "button.sc-blHHSb.dxiEPq"

async def setup():
    browser = await async_playwright().start(headless=False)
    return ForecastExplorerUI(browser.new_page())

async def teardown(browser):
    await browser.close()

if __name__ == "__main__":
    ui = await setup()
    await ui.test_forecast_explorer_ui()
    await teardown(ui.browser)
```

Please note that you need to have the Playwright library installed in your project and import the `LoginPage` from a separate file named `pages/login_page.py`. Here's an example of how the `LoginPage` class can look like:

```python
# src/pages/login_page.py
from playwright.async_api import Page

class LoginPage:
    def __init__(self, page):
        self.page = page

    async def login(self):
        # Implement the login functionality here
```

You will also need to implement the login functionality in the `login` method within the `LoginPage` class based on your website's authentication requirements.