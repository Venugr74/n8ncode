Here is a complete test automation script using Playwright and Python. The script is named `loginTest.py`, and it follows the test steps you've specified, using the provided XPaths:

```python
# loginTest.py

from playwright.sync_api import sync_playwright

def run(playwright):
    # Launch the browser
    browser = playwright.chromium.launch(headless=False)  # Set to True for headless mode
    # Create a new browser context
    context = browser.new_context()
    # Create a new page
    page = context.new_page()

    # Step 1: Open the website
    page.goto("https://www.saucedemo.com")

    # Step 2: Enter credentials
    page.fill('//*[@id="user-name"]', 'standard_user')  # Enter username
    page.fill('//*[@id="password"]', 'secret_sauce')    # Enter password
    page.click('//*[@id="login-button"]')                # Click the login button

    # Optional: Verify if the user is logged in
    assert page.url == "https://www.saucedemo.com/inventory.html", "Login failed"

    # Step 3: Click on the Hamburger Menu Icon on top left
    page.click('//*[@id="react-burger-menu-btn"]')

    # Step 4: Select the logout option
    page.click('//*[@id="logout_sidebar_link"]')

    # Optional: Verify if the user is logged out
    assert page.url == "https://www.saucedemo.com/", "Logout failed"

    # Close the context and the browser
    context.close()
    browser.close()

# Start Playwright
with sync_playwright() as playwright:
    run(playwright)
```

### Explanation of the Script:

1. **Imports**: The script imports `sync_playwright` from Playwright, which allows us to run synchronous operations.

2. **Function Definition**: `run(playwright)` is the main function that performs the test steps.

3. **Launch the Browser**: The browser is launched in non-headless mode (you can change `headless=False` to `headless=True` to run it in the background).

4. **Navigating to URL**: The `goto` method navigates to "https://www.saucedemo.com".

5. **Filling in Credentials**: 
   - The `fill()` method is used to input the username (`standard_user`) and password (`secret_sauce`) into the designated fields using their XPaths.
   - `click()` is used to click the login button.

6. **Login Verification**: An optional assertion checks if the URL matches the expected URL after successful login to ensure the login was successful.

7. **Logout Steps**: 
   - After ensuring the user is logged in, the script clicks on the Hamburger Menu and then on the logout option.

8. **Logout Verification**: Another optional assertion checks if the URL is correct after logging out.

9. **Cleanup**: The context and browser are then closed to end the session.

### Running the Script:
To execute the script, ensure you have Playwright correctly installed:

1. Install Playwright using pip if you haven't already:

   ```bash
   pip install playwright
   ```

2. Install the necessary browser binaries:

   ```bash
   playwright install
   ```

3. Run the script using:

   ```bash
   python loginTest.py
   ```

This script automates the login and logout process for the Sauce Demo website as outlined in your request. You can modify this script further if you want to include additional steps or verifications.