import asyncio
import time
import os

COEFF = 1

async def process_candidate(candidate):
    name, prep1, defense1, prep2, defense2 = candidate
    
    print(f"{name} started the 1 task.")
    await asyncio.sleep(prep1 * COEFF)
    print(f"{name} moved on to the defense of the 1 task.")
    await asyncio.sleep(defense1 * COEFF)
    print(f"{name} completed the 1 task.")
    
    print(f"{name} is resting.")
    await asyncio.sleep(5 * COEFF)
    
    print(f"{name} started the 2 task.")
    await asyncio.sleep(prep2 * COEFF)
    print(f"{name} moved on to the defense of the 2 task.")
    await asyncio.sleep(defense2 * COEFF)
    print(f"{name} completed the 2 task.")

async def interviews(*candidates):
    tasks = [asyncio.create_task(process_candidate(c)) for c in candidates]
    await asyncio.gather(*tasks)

if __name__ == '__main__':
    data = [('Ivan', 5, 2, 7, 2), ('John', 3, 4, 5, 1), ('Sophia', 4, 2, 5, 1)]
    
    t0 = time.time()
    if os.name == 'nt':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    
    asyncio.run(interviews(*data))