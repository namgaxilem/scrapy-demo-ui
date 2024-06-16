from playwright.async_api import async_playwright
import asyncio
import json
import re

auth_data = {"cookies": [{"name": "cookie1", "value": "cookie1 value", "domain": "scrapy-demo-ui.vercel.app", "path": "/", "expires": -1, "httpOnly": False, "secure": True, "sameSite": "Lax"}], "origins": [{"origin": "https://scrapy-demo-ui.vercel.app", "localStorage": [{"name": "item random", "value": "12345"}, {"name": "item hi1122", "value": "hellop"}]}]}
page_url = "https://scrapy-demo-ui.vercel.app"

def extract_local_storage(storage_data):
    lc_obj = {}
    if (storage_data['origins']):
        page_lc_storage = list(filter(lambda item: item.get("origin") == page_url, storage_data['origins']))
        item = next(sub for sub in page_lc_storage if sub)
        if item['localStorage']:
            print("page_lc_storage", item['localStorage'])
            for x in item['localStorage']:
                lc_obj[x['name']] = x['value']
    return lc_obj

async def auto_login_with_localstorage():
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=False)
        browser_context = await browser.new_context(java_script_enabled=True, ignore_https_errors=True)
        await browser_context.add_cookies(auth_data['cookies'])
        lc_obj = extract_local_storage(auth_data)
        
        with open('set_local_storage.js') as f:
            restore_lc_storage_script = f.read()
            restore_lc_storage_script_replace = re.sub(r'data_tobe_replace', json.dumps(lc_obj), restore_lc_storage_script)
            await browser_context.add_init_script(restore_lc_storage_script_replace)
            page = await browser_context.new_page()
            await page.goto(f'{page_url}/about', timeout=0) 
            print("storage_state", json.dumps(await browser_context.storage_state()))
            
        await page.pause()
        
asyncio.run(auto_login_with_localstorage())        