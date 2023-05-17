import asyncio
import aiohttp


async def get_headers(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return url, response.headers.get('content-type')


async def main():
    urls = [
        'https://www.python.org',
        'https://www.google.com',
        'https://github.com',
        'https://stackoverflow.com'
    ]
    tasks = [asyncio.create_task(get_headers(url)) for url in urls]
    headers = await asyncio.gather(*tasks)
    for url, header in headers:
        print(f'URL: {url}\nContent-type: {header}\n')


asyncio.run(main())
