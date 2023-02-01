import asyncio

async def sleep_a_little(time):
    await asyncio.sleep(time)

async def go_do_something():
    time = 1
    await sleep_a_little(time)


asyncio.run(go_do_something())


