Here is the test automation script using Playwright and Python:
```python
import playwright

# Launch the browser
browser = playwright.chromium.launch(headless=False)

# Create a new page
page = browser.new_context().new_page()

# Navigate to the website
page.goto("https://www.saucedemo.com")

# Click on the Login button
page.click("//button[@id='login-button']")

# Enter username and password
page.fill("//input[@id='user-name']", "standard_user")
page.fill("//input[@id='password']", "secret_sauce")

# Click the login button
page.click("//button[@id='login-button']")

# After login, click on the Hamburger Menu Icon
page.click("//button[@id='react-burger-menu-btn']")

# Select the logout option
page.click("//*[id='logout_sidebar_link']")

# Close the browser
browser.close()
```
Let me explain what each line does:

1. `import playwright`: We import the Playwright library.
2. `browser = playwright.chromium.launch(headless=False)`: We launch the Chrome browser in a headless mode (i.e., without a visible browser window).
3. `page = browser.new_context().new_page()`: We create a new page object.
4. `page.goto("https://www.saucedemo.com")`: We navigate to the Saucedemo website.
5. `page.click("//button[@id='login-button']")`: We click on the Login button.
6. `page.fill("//input[@id='user-name']", "standard_user")`: We enter the username "standard_user" into the username input field.
7. `page.fill("//input[@id='password']", "secret_sauce")`: We enter the password "secret_sauce" into the password input field.
8. `page.click("//button[@id='login-button']")`: We click the login button again to submit the form.
9. `page.click("//button[@id='react-burger-menu-btn']")`: We click on the Hamburger Menu Icon.
10. `page.click("//*[id='logout_sidebar_link']")`: We select the logout option from the sidebar.
11. `browser.close()`: We close the browser.

Note that you need to install Playwright and its dependencies using pip:
```
pip install playwright
```
Also, make sure to replace the `chromium` keyword with `firefox` or `webkit` if you want to use a different browser.