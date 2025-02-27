 Here's a basic structure for your `TestScript.py` file located in the `src` directory. I've created a class called `FeatureStoreTest` and a function `test_forecast_explorer_ui`. I've also imported necessary modules, including Playwright and the LoginPage class.

```python
# src/TestScript.py

from playwright.async_api import Playwright, Page
from pages.login_page import LoginPage

async def test_forecast_explorer_ui(playwright: Playwright):
    browser = await playwright.chromium.launch(headless=False)
    context = await browser.newContext()
    page = await context.newPage()

    # Login to the website
    login_page = LoginPage(page)
    await login_page.login()

    # Click Feature Store Icon
    await page.click('span.sc-irPVuy.fYDalG')

    # Click Feature Store Text
    await page.click('//span[normalize-space()="Feature Store"]')

    # Wait for "Launch Feature Job" button to visible
    await page.wait_for_selector('(//button[normalize-space()="Launch Feature Job"])[1]')

    # Click on "Launch Feature Job" Button
    await page.click('(//button[normalize-space()="Launch Feature Job"])[1]')

    # Wait for "Job Selector" button to visible
    await page.wait_for_selector('button.sc-blHHSb.dxiEPq')

    # Verify the "Job Selector" button is visible
    job_selector = await page.$eval('button.sc-blHHSb.dxiEPq', btn => btn.style.display !== 'none')
    assert job_selector is not None, "Job Selector button should be visible."

    # Close the browser
    await browser.close()

# Run the test function
if __name__ == "__main__":
    import asyncio

    asyncio.run(test_forecast_explorer_ui(Playwright()))
```

Please note that you should have a `pages/login_page.py` file with a class `LoginPage`, and the login method implementation. You can find more information on Playwright [here](https://playwright.dev/) and the usage of `headless=False` in browser launching [here](https://playwright.dev/python/docs/api/class-launchoptions).

Don't forget to install Playwright:

```sh
pip install playwright
```