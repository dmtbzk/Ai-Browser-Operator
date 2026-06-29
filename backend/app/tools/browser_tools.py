from app.browser.controller import open_page, search_web
from app.browser.manager import close_browser

def open_browser_page(url: str):
    return open_page(url)

def search_browser_web(query: str):
    return search_web(query)

def close_browser_session():
    close_browser()
    return {"status": "Browser closed"}