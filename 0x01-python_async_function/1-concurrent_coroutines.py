#!/usr/bin/env python3
''' Desc: Import wait_random from the previous python file
    Arg: max_delay: int = 10
'''

import asyncio
from typing import List

from random import uniform
from time import perf_counter


async def wait_random(max_delay: int = 10) -> float:
    delay = uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


async def wait_n(n: int, max_delay: int) -> List[float]:
    tasks = []
    for i in range(n):
        tasks.append(asyncio.create_task(wait_random(max_delay)))
    
    delays = []
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
    
    return delays

