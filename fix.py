import time,asyncio

async def test():
    while True: 
        await asyncio.sleep(2)
        print("ok")


asyncio.run(test())