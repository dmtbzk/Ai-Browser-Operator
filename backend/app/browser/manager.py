from playwright.sync_api import sync_playwright


_playwright = None
_browser = None
_page = None

_browser_state = {
    "current_url": None,
    "current_title": None,
    "last_search_results": [],
}

def get_page():
    global _playwright, _browser, _page

    if _playwright is None:
        _playwright = sync_playwright().start()

    if _browser is None:
        _browser = _playwright.chromium.launch(
            headless=True,
            args=["--no-sandbox", "--disable-blink-features=AutomationControlled"],
        )

    if _page is None:
        context = _browser.new_context(
            user_agent=(
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/124.0.0.0 Safari/537.36"
            ),
            viewport={"width": 1280, "height": 800},
            locale="en-US",
        )
        _page = context.new_page()
        # Hide webdriver flag
        _page.add_init_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

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

def update_browser_state(key: str, value):
    _browser_state[key] = value


def get_browser_state():
    return _browser_state