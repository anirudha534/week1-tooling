import asyncio
import time

import httpx

URLS = [
    "https://httpbin.org/delay/2",
    "https://httpbin.org/delay/2",
]


async def fetch(client: httpx.AsyncClient, url: str) -> int:
    response = await client.get(url)
    return response.status_code


async def main() -> None:
    async with httpx.AsyncClient(timeout=15) as client:
        start = time.perf_counter()
        for url in URLS:
            await fetch(client, url)
        print(f"one by one: {time.perf_counter() - start:.1f}s")

        start = time.perf_counter()
        results = await asyncio.gather(*(fetch(client, url) for url in URLS))
        print(f"together: {time.perf_counter() - start:.1f}s", results)


asyncio.run(main())