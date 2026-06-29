from playwright.sync_api import sync_playwright


_playwright = None
_browser = None
_page = None


def get_page():
    global _playwright, _browser, _page

    if _playwright is None:
        _playwright = sync_playwright().start()

    if _browser is None:
        _browser = _playwright.chromium.launch(headless=False)

    if _page is None:
        _page = _browser.new_page()

    return _page


def close_browser():
    global _playwright, _browser, _page

    if _browser:
        _browser.close()

    if _playwright:
        _playwright.stop()

    _playwright = None
    _browser = None
    _page = None