 Here is a Python script that follows your specifications and uses Playwright:

```python
import time
from playwright.async_api import Playwright, async_playwright

class LoginPage():
    def __init__(self, browser):
        self.browser = browser

    async def login(self):
        # Implement your login functionality here
        pass

async def test_forecast_explorer_ui():
    with await async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()
        login_page = LoginPage(browser)
        await login_page.login()
        # Click Feature Store Icon
        await page.locator("span.sc-irPVuy.fYDalG").click()
        # Click Feature Store Text
        await page.locator('//span[normalize-space()="Feature Store"]').click()
        # Wait for Launch Feature Job button to visible
        await page.wait_for_selector("(//button[normalize-space()=\"Launch Feature Job\"])[1]")
        # Click on Launch Feature Job Button
        launch_job_btn = await page.locator("(//button[normalize-space()=\"Launch Feature Job\"])[1]")
        await launch_job_btn.click()
        # Wait for Job Selector button to visible
        await page.wait_for_selector("button.sc-blHHSb.dxiEPq")
        # Verify the Job Selector button is visible
        assert page.is_visible('button.sc-blHHSb.dxiEPq')

if __name__ == "__main__":
    asyncio.run(test_forecast_explorer_ui())
```

Ensure to install Playwright and create a pages folder with the login_page.py file containing your LoginPage class and login method. Then, you can run this test script using `python src/TestScript.py`.