Here's a complete Playwright test automation script named `loginTest.py` that performs the specified actions on the SauceDemo website. This script will open the website, enter login credentials, log in, and log out using the provided XPaths.

### `loginTest.py`

```python
from playwright.sync_api import sync_playwright

def run(playwright):
    # Launch a browser instance
    browser = playwright.chromium.launch(headless=False)  # Set headless=True for headless testing
    context = browser.new_context()
    page = context.new_page()

    try:
        # Step 1: Open the website
        print("Opening SauceDemo website...")
        page.goto("https://www.saucedemo.com")

        # Step 2: Enter credentials and log in
        print("Entering credentials...")
        page.fill('//*[@id="user-name"]', 'standard_user')  # Enter username
        page.fill('//*[@id="password"]', 'secret_sauce')      # Enter password
        page.click('//*[@id="login-button"]')                  # Click the login button

        # Wait for navigation to complete after logging in
        page.wait_for_navigation(timeout=5000)

        # Step 3: Click on the Hamburger Menu Icon and select the logout option
        print("Logging out...")
        page.click('//*[@id="react-burger-menu-btn"]')        # Click the Hamburger Menu
        page.click('//*[@id="logout_sidebar_link"]')           # Click the Logout option

        # Optionally, validate successful logout
        # Wait for the login button to reappear, indicating the user has logged out
        page.wait_for_selector('//*[@id="login-button"]', timeout=5000)

        print("Logout successful, test completed.")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Close the browser context and the browser
        context.close()
        browser.close()

if __name__ == "__main__":
    with sync_playwright() as playwright:
        run(playwright)
```

### Explanation of the Script:
1. **Imports**: The script imports `sync_playwright` from the Playwright library for running synchronous tests.
2. **Browser Launch**: A Chromium browser instance is launched. Setting `headless=True` can be done if you want to run the test without GUI.
3. **Navigate to the Site**: The script visits the SauceDemo login page.
4. **Login Steps**:
   - It fills in the username and password fields using the provided XPaths.
   - It clicks the login button and waits for navigation to complete.
5. **Logout Steps**:
   - It clicks the Hamburger Menu and selects the logout option.
   - The script waits for the login button to become visible again, indicating the logout was successful.
6. **Error Handling**: The script captures exceptions and prints error messages if any occur during execution.
7. **Cleanup**: The browser context and the browser are closed to release resources properly.

### How to Run the Script
1. Save the code above in a file named `loginTest.py`.
2. Execute the script using the following command:

```bash
python loginTest.py
```

This will automatically perform the login and logout processes on the SauceDemo website as specified. You can adjust the `headless` parameter based on whether you want to see the browser actions in real-time or run the script in the background.