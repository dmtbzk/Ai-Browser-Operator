from app.browser.manager import get_page


def open_page(url: str):
    page = get_page()

    page.goto(url)

    title = page.title()
    current_url = page.url

    page_text = page.locator("body").inner_text(timeout=5000)

    return {
        "title": title,
        "current_url": current_url,
        "short_text": page_text[:1000]
    }


def search_web(query: str):
    page = get_page()

    page.goto("https://duckduckgo.com")

    page.locator("input[name='q']").fill(query)
    page.keyboard.press("Enter")

    page.wait_for_load_state("networkidle")

    results = page.locator("[data-testid='result-title-a']").all()

    search_results = []

    for result in results[:5]:
        search_results.append({
            "title": result.inner_text(),
            "url": result.get_attribute("href")
        })

    return {
        "query": query,
        "results": search_results
    }