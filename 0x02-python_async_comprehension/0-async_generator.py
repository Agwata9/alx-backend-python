#!/usr/bin/env python3
"""a coroutine generator"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """a coroutine that loops 10 times after a wait of 1 second"""
    for _ in range(0, 10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
