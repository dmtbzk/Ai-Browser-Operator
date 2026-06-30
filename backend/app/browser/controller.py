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

    # DuckDuckGo HTML version — no JS, stable selectors, no bot protection
    import urllib.parse
    encoded = urllib.parse.quote_plus(query)
    page.goto(f"https://html.duckduckgo.com/html/?q={encoded}", wait_until="domcontentloaded")

    search_results = []

    result_links = page.locator("a.result__a")
    count = result_links.count()

    for i in range(min(count, 8)):
        link = result_links.nth(i)
        title = link.inner_text().strip()
        href = link.get_attribute("href") or ""

        # DDG HTML wraps real URLs in redirect — extract the actual URL
        if "uddg=" in href:
            import urllib.parse as up
            qs = up.parse_qs(up.urlparse(href).query)
            real_url = qs.get("uddg", [href])[0]
        else:
            real_url = href

        if title and real_url and real_url.startswith("http"):
            search_results.append({"title": title, "url": real_url})

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