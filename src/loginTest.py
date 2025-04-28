Sure! Below is the complete test automation script using Playwright and Python, named `loginTest.py`. The script performs the login and logout operations on the Sauce Demo website based on the specified steps and the provided XPaths.

### `loginTest.py`

```python
# loginTest.py

from playwright.sync_api import sync_playwright

def run(playwright):
    # Step 1: Launch the browser
    browser = playwright.chromium.launch(headless=False)  # Set to True to run in headless mode
    context = browser.new_context()
    page = context.new_page()

    try:
        # Step 2: Open the website
        page.goto("https://www.saucedemo.com")

        # Step 3: Enter credentials
        page.fill('//*[@id="user-name"]', 'standard_user')  # Enter username
        page.fill('//*[@id="password"]', 'secret_sauce')    # Enter password
        page.click('//*[@id="login-button"]')                # Click the login button

        # Step 4: Confirm login
        assert page.url == "https://www.saucedemo.com/inventory.html", "Login failed"

        # Step 5: Click on the Hamburger Menu Icon on top left
        page.click('//*[@id="react-burger-menu-btn"]')

        # Step 6: Select the logout option
        page.click('//*[@id="logout_sidebar_link"]')

        # Step 7: Confirm logout
        assert page.url == "https://www.saucedemo.com/", "Logout failed"
        print("Login and Logout test passed.")
        
    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Close the context and the browser
        context.close()
        browser.close()

# Start Playwright
with sync_playwright() as playwright:
    run(playwright)
```

### Explanation of the Script:

1. **Imports**: The script imports `sync_playwright`, which allows you to control browsers synchronously.

2. **Function Definition**: The `run` function encapsulates the entire test script logic.

3. **Launching the Browser**: 
   - The browser is launched in non-headless mode (you can set `headless=True` if you prefer to run it in the background).
   - A new browser context and page are created for the interaction.

4. **Navigating to the Website**: The `page.goto()` method is used to navigate to "https://www.saucedemo.com".

5. **Filling in Credentials**:
   - The `page.fill()` method is called to enter the username (`standard_user`) and password (`secret_sauce`).
   - The `page.click()` method is used to click the login button.

6. **Login Verification**: An assertion checks if the URL is correct after logging in to ensure that the login was successful.

7. **Logging Out**:
   - After checking that the user is logged in, the script clicks on the Hamburger Menu Icon.
   - Then, it clicks on the logout option in the menu.

8. **Logout Verification**: Another assertion checks if the URL is correct after logging out to confirm that the logout was successful.

9. **Error Handling**: The script includes error handling to catch exceptions and print meaningful error messages.

10. **Cleanup**: The `finally` block ensures that the context and browser are closed properly after the test is completed.

### How to Run the Script:

1. **Install Playwright**: If you have not done so, install the Playwright library:

   ```bash
   pip install playwright
   ```

2. **Install Browsers**: You need to install the required browser binaries needed by Playwright:

   ```bash
   playwright install
   ```

3. **Execute the Script**: Run the script using Python:

   ```bash
   python loginTest.py
   ```

This script automates the entire login and logout process for the Sauce Demo website, adhering to the instructions and XPath selectors you provided. You can further expand the script by adding more tests or functionalities as needed.