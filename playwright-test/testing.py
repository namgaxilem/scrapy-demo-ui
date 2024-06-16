from playwright.async_api import async_playwright
import asyncio

async def auto_login_with_localstorage():
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=False)
        browser_context = await browser.new_context(java_script_enabled=True, ignore_https_errors=True)
        
        with open('set_local_storage.js') as f:
            lcStorage = f.read()
            page = await browser_context.new_page()
            page.evaluate(lcStorage, '{"qvo" : "Value random"}')
            
        await page.goto("https://scrapy-demo-ui.vercel.app/about", timeout=0) 
        await asyncio.sleep(20)   
        
asyncio.run(auto_login_with_localstorage())        