#!/usr/bin/env python3
'''
Wait for random durations and return the delay times in a list.
'''
import asyncio
import random
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random
tak_3 = __import__('3-tasks').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''
    Create multiple tasks that wait for random durations with max delay.

    Args:
        n (int): The number of times to create tasks.
        max_delay (int): The maximum delay time (in milliseconds) for each task

    Returns:
        List[float]: A list of delay times (float values) in ascending order.
    '''
    tasks = [tak_3(max_delay) for _ in range(n)]
    delays = [await task for task in asyncio.as_completed(tasks)]
    return delays
