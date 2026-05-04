import asyncio


class AsyncDBConn:
    def __init__(self, db_name):
        self.db_name = db_name
    
    async def __aenter__(self):
        # await asyncio.sleep(1)
        # self.connection = self.db_name + "_connection"
        for _ in range(10):
             await asyncio.sleep(1)
             print(f"trying to connect to: {self.db_name}")
        # return f"made connection to {self.db_name}"
    
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await asyncio.sleep(1)
        if exc_type:
            return f"closed connection to, error: {exc_val}"
    
async def main():
        async with AsyncDBConn("Prod_DB") as conn:
            print(f"Using conn: {conn}")

async def ticker():
     for _ in range(10):
          print(f"ticker started")
          await asyncio.sleep(1)
          print(f"ticker ended")


async def parernt():
    task1 = asyncio.create_task(main())
    task2 = asyncio.create_task(ticker())
    await asyncio.wait([task1, task2])

asyncio.run(parernt())

