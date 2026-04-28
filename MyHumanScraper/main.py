import asyncio
import random
from playwright.async_api import async_playwright


async def run_scraper():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)


        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )

        page = await context.new_page()

        print("[*] Navigating like a human...")
        await page.goto("https://quotes.toscrape.com", wait_until="networkidle")


        await asyncio.sleep(random.uniform(2, 4))


        quotes = await page.query_selector_all(".quote")

        print(f"\n--- Found {len(quotes)} Quotes ---\n")

        for quote in quotes:
            text_element = await quote.query_selector(".text")
            author_element = await quote.query_selector(".author")

            text = await text_element.inner_text()
            author = await author_element.inner_text()

            print(f"“{text}” - {author}")

        print("\n[*] Task complete. Closing browser...")
        await asyncio.sleep(2)
        await browser.close()


if __name__ == "__main__":
    asyncio.run(run_scraper())