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