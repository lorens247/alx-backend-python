#!/usr/bin/env python3
'''Create an asyncio.Task for waiting a random time'''
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    '''
    Create an asyncio.Task that waits for a random duration.

    Args:
        max_delay (int): The maximum delay time (in milliseconds) for waiting.

    Returns:
        asyncio.Task: A Task representing the asynchronous operation of waiting
                        for a random duration with a maximum delay of max_delay
    '''
    return asyncio.create_task(wait_random(max_delay))
