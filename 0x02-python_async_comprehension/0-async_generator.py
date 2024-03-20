#!/usr/bin/env python3
'''
The coroutine will loop 10 times, each time asynchronously wait 1 second, 
then yield a random number between 0 and 10. Use the random module. 
'''
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]: # type: ignore
    '''
    Asynchronous generator that yields random numbers with a delay.

    Yields:
        float: A random float between 0 and 10.

    Usage:
        async for num in async_generator():
            print(num)
    '''
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
