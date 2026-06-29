from playwright.sync_api import sync_playwright

def open_page(url: str):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(url)
        title = page.title()
        current_url = page.url
        browser.close()
        return {
            "title": title,
            "current_url": current_url
        }

