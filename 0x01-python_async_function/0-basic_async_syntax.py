#!/usr/bin/env python3
''' Desc: asynchronous coroutine that takes in an integer argument
    Arg: max_delay: int = 10
'''

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    ''' Wait up to max_delay then return length of delay. '''
    delay = max_delay * random.random()
    await asyncio.sleep(delay)
    return delay
