import asyncio
import time


async def make_toast() -> str:
    print("toast started")
    await asyncio.sleep(2)
    print("toast done")
    return "toast"


async def boil_egg() -> str:
    print("egg started")
    await asyncio.sleep(5)
    print("egg done")
    return "egg"


async def main() -> None:
    start = time.perf_counter()
    toast, egg = await asyncio.gather(make_toast(), boil_egg())
    print(toast, egg)
    print(f"took {time.perf_counter() - start:.1f} seconds")


asyncio.run(main())

