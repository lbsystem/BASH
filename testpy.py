#!/usr/bin/python3
import socket,requests,asyncio

# res=requests.get("https://www.china.com",verify=False)
# print(res.content.decode())

async def test():
    print("start")
    await asyncio.sleep(6)



asyncio.run(test())