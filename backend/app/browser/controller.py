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
    import urllib.parse
    import random
    import time

    page = get_page()

    encoded = urllib.parse.quote_plus(query)
    page.goto(
        f"https://www.google.com/search?q={encoded}&hl=en",
        wait_until="domcontentloaded",
    )

    # Human-like delay
    time.sleep(random.uniform(1.5, 2.5))

    search_results = []

    # Google organic result links sit inside <h3> inside <a>
    anchors = page.locator("a:has(h3)")
    count = anchors.count()

    for i in range(count):
        a = anchors.nth(i)
        try:
            href = a.get_attribute("href") or ""
            title = a.locator("h3").inner_text(timeout=500).strip()
            # Skip Google internal / ad links
            if href.startswith("http") and title and "google.com" not in href:
                search_results.append({"title": title, "url": href})
            if len(search_results) >= 8:
                break
        except Exception:
            continue

    update_browser_state("last_search_results", search_results)
    update_browser_state("current_url", page.url)
    update_browser_state("current_title", page.title())

    return {"query": query, "results": search_results}

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