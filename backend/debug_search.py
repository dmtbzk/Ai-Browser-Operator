from playwright.sync_api import sync_playwright
import urllib.parse, time, random

query = "OpenAI Operator"
encoded = urllib.parse.quote_plus(query)

with sync_playwright() as p:
    browser = p.chromium.launch(
        headless=True,
        args=["--no-sandbox", "--disable-blink-features=AutomationControlled"],
    )
    context = browser.new_context(
        user_agent=(
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/124.0.0.0 Safari/537.36"
        ),
        viewport={"width": 1280, "height": 800},
        locale="en-US",
    )
    page = context.new_page()
    page.add_init_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

    page.goto(f"https://www.google.com/search?q={encoded}&hl=en", wait_until="domcontentloaded")
    time.sleep(random.uniform(1.5, 2.5))

    print("Title:", page.title())

    anchors = page.locator("a:has(h3)")
    count = anchors.count()
    print(f"a:has(h3) count: {count}")

    for i in range(min(count, 8)):
        a = anchors.nth(i)
        try:
            href = a.get_attribute("href") or ""
            title = a.locator("h3").inner_text(timeout=500).strip()
            if href.startswith("http") and "google.com" not in href:
                print(f"  [{i}] {title[:60]} -> {href[:80]}")
        except Exception as e:
            print(f"  [{i}] error: {e}")

    browser.close()
