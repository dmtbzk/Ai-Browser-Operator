from app.browser.manager import get_page, update_browser_state

def open_page(url: str):
    page = get_page()

    page.goto(url)

    title = page.title()
    current_url = page.url

    page_text = page.locator("body").inner_text(timeout=5000)

    update_browser_state("current_url", current_url)
    update_browser_state("current_title", title)

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

    update_browser_state("last_search_results", search_results)
    update_browser_state("current_url", page.url)
    update_browser_state("current_title", page.title())

    return {
        "query": query,
        "results": search_results
    }

def extract_links():
    page = get_page()
    links = page.locator("a").all()
    extracted_links = []
    for link in links[:30]:
        text = link.inner_text()
        href = link.get_attribute("href")
        if href:
            extracted_links.append({
                "text": text,
                "href": href
            })
    return {
        "current_url": page.url,
        "links": extracted_links
    }