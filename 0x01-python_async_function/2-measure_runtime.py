#!/usr/bin/env python3
'''runtime measure'''
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''
    Measure the average time it takes to execute the wait_n
    function multiple times concurrently.
    Args:
        n (int): The number of times to execute the wait_n function.
        max_delay (int): The maximum delay time for each execution of wait_n.
    Returns:
        float: The average time (in s) it takes for each execution of wait_n.
    '''
    s = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    elapsed = time.perf_counter() - s
    return elapsed / n
