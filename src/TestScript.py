 Here's a basic structure for your test script `TestScript.py` in the given path `src/TestScript.py`. I'll be using the Pytest framework and Playwright to create this test. Make sure you have installed these dependencies before running the script.

```python
import pytest
from playwright.async_api import Playwright, async_playwright

# pages.py
from playwright.async_api import Page

class LoginPage:
    def __init__(self, page):
        self.page = page

    @staticmethod
    async def login():
        # Implement the login logic here
        pass

# src/pages/feature_store_page.py
from playwright.async_api import Page

class FeatureStorePage:
    def __init__(self, page):
        self.page = page

    async def is_visible(self, selector):
        await self.page.wait_for_selector(selector)

    async def click(self, selector):
        await self.page.click(selector)

# src/TestScript.py
import pytest
from pages import LoginPage, FeatureStorePage

@pytest.fixture(scope="function")
async def browser():
    browser = await async_playwright().start()
    context = await browser.new_context(headless=False)
    page = await context.new_page()
    yield page
    await context.close()
    await browser.close()

@pytest.mark.asyncio
async def test_forecast_explorer_ui():
    with async_playwright() as pw:
        browser = await pw.launch(headless=False)
        page = await LoginPage.login(await browser.new_page())
        featureStorePage = FeatureStorePage(page)

        # Click the Feature Store Icon
        await featureStorePage.click("span.sc-irPVuy.fYDalG")

        # Click the Feature Store Text
        await featureStorePage.click("//span[normalize-space()='Feature Store']")

        # Wait for Launch Feature Job button to visible
        await featureStorePage.is_visible("(//button[normalize-space()="Launch Feature Job"])[1]")

        # Click on the Launch Feature Job Button
        await featureStorePage.click("(//button[normalize-space()="Launch Feature Job"])[1]")

        # Wait for Job Selector button to visible
        await featureStorePage.is_visible("button.sc-blHHSb.dxiEPq")

        # Verify the Job Selector button is visible
        assert True, "Job Selector button not found"
```

This script creates a LoginPage class that logs into the website and a FeatureStorePage class that interacts with the feature store page of the web application. The test function `test_forecast_explorer_ui` uses these classes to log in, navigate to the feature store, click the necessary buttons, wait for elements to be visible, and verify if the job selector button is present on the page.

Please replace the comments inside the LoginPage class with your actual login logic and adapt the script according to your web application's structure and naming conventions.