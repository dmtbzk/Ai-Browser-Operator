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

def search_web(query: str):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://duckduckgo.com")

        page.locator("input[name='q']").fill(query)
        page.keyboard.press("Enter")

        page.wait_for_load_state("networkidle")

        results = page.locator("[data-testid='result-title-a']").all()

        search_results = []

        for result in results[:5]:
            title = result.inner_text()
            url = result.get_attribute("href")

            search_results.append({
                "title": title,
                "url": url
            })

        browser.close()

        return {
            "query": query,
            "results": search_results
        }
