Below is a complete Playwright test automation script written in Python, named `loginTest.py`. This script opens the Sauce Demo website, logs in using the provided credentials, logs out, and effectively utilizes the specified XPaths for interaction with the elements.

### `loginTest.py`

```python
from playwright.sync_api import sync_playwright

def run(playwright):
    # Launch the browser (set headless=True to run in the background)
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    
    try:
        # Step 1: Open the Sauce Demo website
        page.goto("https://www.saucedemo.com")

        # Step 2: Enter username as 'standard_user'
        page.fill('//*[@id="user-name"]', 'standard_user')

        # Step 3: Enter password as 'secret_sauce'
        page.fill('//*[@id="password"]', 'secret_sauce')

        # Step 4: Click on the Login button
        page.click('//*[@id="login-button"]')

        # Wait for navigation to complete
        page.wait_for_navigation()

        # Step 5: Click on the Hamburger Menu Icon on the top left
        page.click('//*[@id="react-burger-menu-btn"]')

        # Step 6: Select the logout option
        page.click('//*[@id="logout_sidebar_link"]')

        # Wait for navigation after logging out
        page.wait_for_navigation()

    finally:
        # Step 7: Close the browser
        browser.close()

if __name__ == "__main__":
    with sync_playwright() as playwright:
        run(playwright)
```

### Instructions to Run the Script

1. **Install Python and Playwright**:
   Make sure you have Python installed. You can install Playwright as follows:

   ```bash
   pip install playwright
   ```

2. **Install Browser Binaries**:
   After installing Playwright, you need to install the necessary browser binaries:

   ```bash
   playwright install
   ```

3. **Save the Script**:
   Save the above Python script code in a file named `loginTest.py`.

4. **Run the Script**:
   Open a terminal or command prompt, navigate to the directory where `loginTest.py` is located, and execute the script with:

   ```bash
   python loginTest.py
   ```

### Explanation of the Script:

- **Imports**: The script imports the necessary modules from the Playwright library.
- **Browser Launching**: The Chromium browser is launched in normal mode (set `headless=True` to run it in the background).
- **Navigation to the Site**: The script navigates to the Sauce Demo website.
- **User Interaction**: 
  - Fills in the username and password fields.
  - Clicks the login button.
  - After a successful login, clicks on the hamburger menu and selects the logout option.
- **Cleanup**: The script ensures the browser closes after the test completes.

This automated script performs the end-to-end login and logout functionality as you specified and utilizes the provided XPaths accurately.