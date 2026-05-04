# import asyncio
# import time


# async def apiCaller(model_name):
#     print(f"api callled started by {model_name}")
#     await asyncio.sleep(2)
#     print(f"api callled finished by {model_name}")

# async def main():
#     startedAt = time.perf_counter()

#     print(f"Started at {startedAt}")

#     result1 = await apiCaller("Model-1")
#     result2 = await apiCaller("Model-2")

#     print(f"Returned At {time.perf_counter() - startedAt}")

# if __name__ == "__main__":
#     asyncio.run(main())

import asyncio
import time

async def call_llm(agent_name):
    print(f"[{agent_name}] Sending prompt to LLM...")
    # Simulate the delay of an API call (2 seconds)
    await asyncio.sleep(2) 
    print(f"[{agent_name}] Received response from LLM.")
    return f"{agent_name} result"

async def main():
    start_time = time.perf_counter()

    # We start both tasks "concurrently"
    print("Starting Agentic Workflow...")
    
    # asyncio.gather runs them at the same time
    results = await asyncio.gather(
        call_llm("Agent_A"),
        call_llm("Agent_B")
    )

    end_time = time.perf_counter()
    print(f"Results: {results}")
    print(f"Total time: {end_time - start_time:.2f} seconds")

# To run the top-level entry point
if __name__ == "__main__":
    asyncio.run(main())