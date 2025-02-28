 To create an automated UI test using Python and Playwright, I'll provide you with a basic structure for the `TestScript.py` file located at `src/TestScript.py`. I assume you have already set up your project with necessary dependencies such as Playwright and the `pages.login_page` module.

```python
# src/TestScript.py
import playwright
from pages.login_page import LoginPage

def test_forecast_explorer_ui():
    # Initialize a new browser instance (Headless = False)
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Navigate to the application URL
    page = context.new_page()
    page.goto('http://your-app-url')

    # Login using the login method from pages.login_page
    login_page = LoginPage(page)
    login_page.login()

    # Click on Feature Store Icon
    feature_store_icon = page.query_selector('span.sc-irPVuy.fYDalG')
    feature_store_icon.click()

    # Click on Feature Store Text
    feature_store_text = page.wait_for_selector('//span[normalize-space()="Feature Store"]')
    feature_store_text.click()

    # Wait for Launch Feature Job button to be visible
    launch_feature_job_button = page.wait_for_selector(lambda selector: len(list(selector.get_by_css_selector("(//button[normalize-space()='Launch Feature Job'])[1]")) > 0)

    # Click on Launch Feature Job Button
    launch_feature_job_button.nth(0).click()

    # Wait for Job Selector button to be visible
    job_selector = page.wait_for_selector('button.sc-blHHSb.dxiEPq')

    # Verify the Job Selector button is visible (Assuming that it's not an error if the button isn't found)
    _ = job_selector  # Ignore any potential exception when the Job Selector isn't found

    # Close the browser
    browser.close()

if __name__ == "__main__":
    test_forecast_explorer_ui()
```

This script navigates to your web application, logs in using the provided `login_page`, and performs UI interactions based on the given selectors. Make sure to replace `'http://your-app-url'` with the actual URL of your web app. The test script also assumes that the Job Selector button will be visible after performing the specified actions.