from playwright.sync_api import sync_playwright
import config
with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)

    page = browser.new_page()

    page.goto("https://practicetestautomation.com/practice-test-login/")
    
    page.fill("#username", config.USERNAME)
    page.fill("#password", config.PASSWORD)
    page.click("#submit")
    text = page.get_by_role("heading", name="Logged In Successfully").text_content()
    
    if(text == "Logged In Successfully"):
        print("Logged In Successfully")
    
    page.get_by_role("link", name= "Log out").click()
    