#!/usr/bin/env python3
'''
The coroutine will collect 10 random numbers using an async comprehensing
over async_generator, then return the 10 random numbers.
'''
import asyncio
from typing import List
asyngen = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''
    Asynchronous comprehension to collect values from an async generator.

    Returns:
        list: A list containing the values yielded by the async generator.

    Usage:
        result = await async_comprehension()
    '''
    return [i async for i in asyngen()]
