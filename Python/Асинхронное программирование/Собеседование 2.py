import asyncio
import time
import os

COEFF = 0.1


async def task_work(name, prep_t, def_t, task_num):
    print(f'{name} started the {task_num} task.')
    await asyncio.sleep(prep_t * COEFF)

    print(f'{name} moved on to the defense of the {task_num} task.')
    await asyncio.sleep(0.1 * COEFF)

    print(f'{name} completed the {task_num} task.')


async def process_candidate(candidate, task1_event, task2_event):
    name, prep1, defense1, prep2, defense2 = candidate
    
    await task1_event.wait()
    await task_work(name, prep1, defense1, 1)

    await task2_event.wait()
    await task_work(name, prep2, defense2, 2)


async def interviews_2(*candidates):
    task1_event = asyncio.Event()
    task2_event = asyncio.Event()

    task1_event.set()

    await asyncio.sleep(0.1 * COEFF)

    task2_event.set()

    tasks = [asyncio.create_task(process_candidate(c, task1_event, task2_event)) for c in candidates]
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    data = [('Ivan', 5, 2, 7, 2), ('John', 3, 4, 5, 1), ('Sophia', 4, 2, 5, 1)]
    
    t0 = time.time()
    if os.name == 'nt':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    
    asyncio.run(interviews_2(*data))