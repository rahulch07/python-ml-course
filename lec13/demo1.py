import asyncio
import time


async def file_coroutine(sleep=5):
    print(f"coroutine file started at: {time.time()}")
    await asyncio.sleep(sleep)
    print(f"coroutine file ended at: {time.time()}")

async def api_coroutine(sleep=5):
    print(f"coroutine api started at: {time.time()}")
    await asyncio.sleep(sleep)
    print(f"coroutine api ended at: {time.time()}")

async def main():
    task1 = asyncio.create_task(file_coroutine(sleep=2))
    task2 = asyncio.create_task(api_coroutine(sleep=3))

    await asyncio.sleep(1)
    task1.cancel()

    done, pending = await asyncio.wait([task1, task2])
    print(f"done: {done}, pending: {pending}")

# asyncio.run(main())

# count = 0
# async def incrementer1(sleep=0.1):
#     global count
#     for _ in range(10):
#         temp = count
#         await asyncio.sleep(sleep)
#         temp += 1
#         count = temp

# async def parent():
#     await asyncio.gather(incrementer1(sleep=0.1), incrementer1(sleep=0.15))

# asyncio.run(parent())

# print(f"count: {count}")



async def fib():
    a, b = 0,1
    for _ in range(10):
        yield a
        await asyncio.sleep(1)
        a, b = b, a+b

async def display_fib():
    async for val in fib():
        print(val)


async def main2():
    task1 = asyncio.create_task(display_fib())
    task2 = asyncio.create_task(api_coroutine(sleep=1))

    # await asyncio.sleep(1)
    # task1.cancel()

    done, pending = await asyncio.wait([task1, task2])
    print(f"done: {done}, pending: {pending}")

asyncio.run(main2())

