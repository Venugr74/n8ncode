 Here's an example of how you can write an automated UI test using Python and Playwright to verify the functionality of a web application as per your requirements. I've created a file named `TestScript.py` in the directory `src`.

```python
# src/TestScript.py

import time
from playwright.sync_api import sync_playwright, expect
from pages.login_page import LoginPage

def test_forecast_explorer_ui():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Login to the website
        login_page = LoginPage(page)
        login_page.login()

        # Navigate to Feature Store
        page.waitForSelector('span.sc-irPVuy.fYDalG').click()
        page.waitForSelector('//span[normalize-space()="Feature Store"]').click()

        # Wait for "Launch Feature Job" button to visible
        page.waitForSelector('(//button[normalize-space()="Launch Feature Job"])[1]')

        # Click on "Launch Feature Job" Button
        launch_feature_job_btn = page.querySelector('(//button[normalize-space()="Launch Feature Job"])[1]')
        launch_feature_job_btn.click()

        # Wait for "Job Selector" button to visible and verify it's visible
        expect(page.querySelector(JobSelector)).toBeVisible()

        # Close the browser
        browser.close()
```

This test script does the following:
- Launches a non-headless browser using Chromium
- Logs in to the website using the `login_page` class from `pages.login_page` and the `login` method
- Navigates to the Feature Store
- Waits for the "Launch Feature Job" button and clicks it
- Waits for the "Job Selector" button and verifies that it's visible using expect() assertion
- Closes the browser when done

Make sure to replace `JobSelector` with your actual job selector value.

You should also create a folder named `pages` where you define your pages, in this case, the `login_page`. Here's an example of how to implement the `LoginPage` class:

```python
# pages/login_page.py
from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page):
        self.page = page

    def login(self):
        # Locate the username and password fields and login button using their selectors
        self.page.waitForSelector('//input[@name="username"]')
        self.page.waitForSelector('//input[@name="password"]')
        self.page.waitForSelector('//button[normalize-space()="Login"]')

        # Fill in the username and password fields
        self.page.fill('//input[@name="username"]', 'your_username')
        self.page.fill('//input[@name="password"]', 'your_password')

        # Click on the login button
        self.page.click('//button[normalize-space()="Login"]')
```