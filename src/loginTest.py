To create a test automation script using Playwright and Python that follows the specified steps for logging into the website "https://www.saucedemo.com", we'll write a script named `loginTest.py`. This script will perform the login operation using the provided credentials, and then proceed to log out. Below is the complete code for the script:

```python
# loginTest.py

from playwright.sync_api import sync_playwright

def run(playwright):
    # Launch the browser
    browser = playwright.chromium.launch(headless=False)
    # Open a new browser context
    context = browser.new_context()
    # Create a new page
    page = context.new_page()

    # Step 1: Open the website
    page.goto("https://www.saucedemo.com")

    # Step 2: Click on the Login button and enter credentials
    page.fill('//*[@id="user-name"]', 'standard_user')  # Enter username
    page.fill('//*[@id="password"]', 'secret_sauce')    # Enter password
    page.click('//*[@id="login-button"]')                # Click the login button

    # Step 3: Click on the Hamburger Menu Icon on top left
    page.click('//*[@id="react-burger-menu-btn"]')

    # Step 4: Select the logout option
    page.click('//*[@id="logout_sidebar_link"]')

    # Optional: You might want to verify if the logout was successful by checking the URL or an element
    # For example:
    # assert page.url == "https://www.saucedemo.com/"

    # Close the browser context and the browser
    context.close()
    browser.close()

# Start Playwright
with sync_playwright() as playwright:
    run(playwright)
```

### Explanation of the Code:

1. **Imports**: The script imports `sync_playwright` from the `playwright.sync_api` module. This allows us to use synchronous Playwright features in our script.

2. **Function Definition**: The `run` function contains the main automation logic.

3. **Launching the Browser**: A Chromium browser instance is created and launched in non-headless mode (you can set `headless=True` to run in headless mode).

4. **Navigating to the URL**: The `goto` method is used to navigate to "https://www.saucedemo.com".

5. **Interaction with Input Fields**: The `fill` method is used to input the username and password using the XPaths provided in the question.

6. **Login Action**: The script clicks the login button using the provided XPath.

7. **Logout Process**: After logging in, we click the Hamburger Menu and log out using the provided XPaths.

8. **Cleanup**: Finally, we close the browser context and the browser itself.

### Running the Script:
To run the script, make sure you have Playwright installed. You can install it using pip:

```bash
pip install playwright
```

Then, install the required browser binaries:

```bash
playwright install
```

After that, simply run the `loginTest.py` script:

```bash
python loginTest.py
```

This script will execute the login and logout process as specified.