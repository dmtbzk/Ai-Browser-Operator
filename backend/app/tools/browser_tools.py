from app.browser.controller import open_page, search_web
from app.browser.manager import close_browser, get_browser_state

def open_browser_page(url: str):
    return open_page(url)

def search_browser_web(query: str):
    return search_web(query)

def close_browser_session():
    close_browser()
    return {"status": "Browser closed"}

def get_current_browser_state():
    return get_browser_state()

def open_search_result(index: int):

    state = get_browser_state()
    results = state.get("last_search_results", [])

    if not results:
        return {"error": "No search results available"}
    if index < 1 or index > len(results):
        return {"error": "Invalid result index"}
    
    selected_result = results[index - 1]

    url = selected_result["url"]

    return open_page(url)

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