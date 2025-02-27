 Here is the code for the `TestScript.py` file in the given path `src/TestScript.py`. I have used Playwright for automated UI testing and followed the given selectors and class names:

```python
import time
from playwright.async_api import Playwright, async_playwright
from pages.login_page import LoginPage

class ForecastExplorerUI:
    def __init__(self, browser):
        self.browser = browser
        self.page = browser.new_page()

    async def test_forecast_explorer_ui(self):
        await self.login_page.login()  # Call login method from pages.login_page

        # Click Feature Store Icon
        await self.page.click('span.sc-irPVuy.fYDalG')

        # Click Feature Store Text
        await self.page.click('//span[normalize-space()="Feature Store"]')

        # Wait for Launch Feature Job button to visible
        await self.page.wait_for_selector("(//button[normalize-space()='Launch Feature Job'])[1]")

        # Click on Launch Feature Job Button
        launch_feature_job_button = await self.page.$x("(//button[normalize-space()='Launch Feature Job'])[1]")
        await launch_feature_job_button[0].click()

        # Wait for Job Selector button to visible
        await self.page.wait_for_selector("button.sc-blHHSb.dxiEPq")

        # Verify the Job Selector button is visible
        job_selector = await self.page.$x("button.sc-blHHSb.dxiEPq")
        assert len(job_selector) > 0, "Job Selector button is not visible"

async def main():
    browser = await async_playwright().start(headless=False)
    login_page = LoginPage(browser)
    forecast_explorer_ui = ForecastExplorerUI(login_page)

    try:
        await forecast_explorer_ui.test_forecast_explorer_ui()
    except Exception as e:
        print(f"Test failed with error: {e}")
    finally:
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
```

In this example, I have created a `ForecastExplorerUI` class to handle the UI test for the given features and used Playwright to synchronize the browser and run the tests in an asynchronous manner. The main function initializes the browser, creates instances of LoginPage and ForecastExplorerUI classes, and runs the test using the test_forecast_explorer_ui method.