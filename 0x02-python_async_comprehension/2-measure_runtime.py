#!/usr/bin/env python3
'''
Import async_comprehension from the previous file and write a 
measure_runtime coroutine that will execute async_comprehension 
four times in parallel using asyncio.gather
'''
import time
import asyncio
asynccomp = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''
    Measures the total execution time of running async_comprehension()
    4 times concurrently.

    Returns:
    float: The total execution time in seconds.
    '''
    start_time = time.time()
    tasks = [asynccomp() for _ in range(4)]
    await asyncio.gather(*tasks)
    end_time = time.time()
    execution_time = end_time - start_time
    return execution_time
