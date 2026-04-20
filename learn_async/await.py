
import asyncio
#from fastapi import FastAPI

#app = FastAPI

#@app.get("/")
#async def root():
#    return {"m": "a"}


async def fetch_data(delay):
    print("fetching data")
    await asyncio.sleep(delay)
    print("Data fetched")
    return {"data": "some data"}

async def main():
    print("main coroutine")
    task = fetch_data(2)

    res = await task
    print(f"Received data: {res}")
    print("End of main coroutine")

asyncio.run(main())
