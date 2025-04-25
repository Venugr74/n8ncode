Here’s a complete test automation script using Playwright in Python, named `loginTest.py`. This script will perform the actions you specified: it will open the Sauce Demo website, enter credentials, log in, and then log out using the provided XPaths.

### `loginTest.py`

```python
import os
from playwright.sync_api import sync_playwright

def run(login_user, login_pass):
    with sync_playwright() as p:
        # Launch the browser (set headless to True for background running)
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        # Step 1: Open Sauce Demo website
        page.goto("https://www.saucedemo.com")
        
        # Step 2: Enter username
        page.fill('//*[@id="user-name"]', login_user)
        
        # Step 3: Enter password
        page.fill('//*[@id="password"]', login_pass)
        
        # Step 4: Click on the login button
        page.click('//*[@id="login-button"]')
        
        # Wait for the page to load before interacting with the menu
        page.wait_for_timeout(2000)  # Waits for 2 seconds (optional)

        # Step 5: Click on the Hamburger Menu Icon
        page.click('//*[@id="react-burger-menu-btn"]')
        
        # Step 6: Select the logout option
        page.click('//*[@id="logout_sidebar_link"]')

        # Optional: Wait to observe the logout action
        page.wait_for_timeout(2000)  # waits for 2 seconds (optional)

        # Close the browser
        browser.close()

# Run the test with specified credentials
if __name__ == "__main__":
    run("standard_user", "secret_sauce")
```

### Explanation of the Script:
1. **Imports**: The script imports the necessary modules from Playwright.
   
2. **Function Definition**: The `run` function takes `login_user` and `login_pass` as arguments to perform automation tasks.
   
3. **Browser Launch**: The script launches a Chromium browser. You can set `headless=True` if you want to run it in the background (without a visible browser window).

4. **Navigation and Login**:
   - It navigates to `https://www.saucedemo.com`.
   - It fills in the username and password fields using the provided XPaths.
   - After providing the credentials, it clicks the login button.

5. **Logout Procedure**:
   - After waiting a brief moment to ensure the page loads completely, it clicks the hamburger menu and selects the logout option.

6. **Closure**: The script waits a bit to allow for observation of the logout action and then closes the browser.

### Running the Script:
1. Make sure you have Playwright installed. If you haven’t already, you can install it using pip:

   ```bash
   pip install playwright
   playwright install
   ```

2. Save the script as `loginTest.py`.

3. Run the script from your command line:

   ```bash
   python loginTest.py
   ```

This will execute the automation steps as outlined, logging into the Sauce Demo site as `standard_user` and then logging out. Adjust the XPath expressions and wait times as necessary based on the performance of the website.