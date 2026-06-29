from app.browser.controller import open_page, search_web

def open_browser_page(url: str):
    return open_page(url)

def search_browser_web(query: str):
    return search_web(query)