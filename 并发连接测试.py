import asyncio,aiohttp
from asyncio import tasks
import requests
from async_timeout import timeout

# async def req():
#     print("start")
#     async with aiohttp.ClientSession() as session:
#         await session.get("http://192.168.1.32:7890",timeout=20)
#         print(await session.headers())
#         await session.close()
        


# async def main():
#     loop=asyncio.get_event_loop()
#     tasks=[]
#     for i in range(35):
#         tasks.append(loop.create_task(req()))

#     await asyncio.wait(tasks)


# asyncio.run(main())
        
res=requests.get("http://192.168.1.32:7890")
print(res.headers)