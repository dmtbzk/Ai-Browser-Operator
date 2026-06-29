from playwright.sync_api import sync_playwright

def open_page(url: str):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(url)
        title = page.title()
        current_url = page.url
        page_text = page.locator("body").inner_text(timeout=5000)
        short_text = page_text[:1000]

        browser.close()
        return {
            "title": title,
            "current_url": current_url,
            "short_text": short_text
        }


