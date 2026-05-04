import asyncio


async def file_coroutine(sleep=5):
    print("coroutine file started")
    await asyncio.sleep(sleep)
    print("coroutine file ended")

async def api_coroutine(sleep=1):
    print("coroutine api started")
    await asyncio.sleep(sleep)
    print("coroutine api ended")

async def main():
    await asyncio.gather(file_coroutine(), api_coroutine())

# asyncio.run(main())

count = 0
async def incrementer1(sleep=0.1):
    global count
    for _ in range(10):
        temp = count
        await asyncio.sleep(sleep)
        temp += 1
        count = temp

async def parent():
    await asyncio.gather(incrementer1(sleep=0.1), incrementer1(sleep=0.15))

# asyncio.run(parent())
asyncio.run(incrementer1())

print(f"count: {count}")