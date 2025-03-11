 Here's an example of how you could structure your `TestScript.py` file in the given directory (`src/TestScript.py`) using Python and Playwright to perform the specified UI tests:

```python
from playwright.async_api import Playwright, async_playwright
import time
from pages.login_page import LoginPage

async def test_forecast_explorer_ui(playwright):
    browser = await playwright.chromium.launch(headless=False)
    context = await browser.newContext()
    page = await context.newPage()

    # Login to the website
    login_page = LoginPage(page)
    await login_page.login()

    # Click on Feature Store Icon
    await page.click('span.sc-irPVuy.fYDalG')

    # Click on Feature Store Text
    await page.click('//span[normalize-space()="Feature Store"]')

    # Wait for Launch Feature Job button to be visible
    await page.wait_for_selector("(//button[normalize-space()='Launch Feature Job'])[1]")

    # Click on Launch Feature Job Button
    await page.click("(//button[normalize-space()='Launch Feature Job'])[1]")

    # Wait for Job Selector button to be visible
    await page.wait_for_selector("button.sc-blHHSb.dxiEPq")

    # Verify the Job Selector button is visible
    job_selector = await page.$x("button.sc-blHHSb.dxiEPq")
    assert len(job_selector) > 0, "Job Selector button not found"

    await browser.close()

async def main():
    playwright = await async_playwright.start()
    await test_forecast_explorer_ui(playwright)

if __name__ == "__main__":
    asyncio.run(main())
```

In this example, I've imported the `LoginPage` class from a separate file `pages/login_page.py`, and created an asynchronous function called `test_forecast_explorer_ui`. This function sets up the browser using Playwright, logs in to the website with the `login_page.login()` method, performs the required UI tests, and verifies that the Job Selector button is visible.

The main function starts the Playwright, runs the test function, and closes the browser after the test has finished.