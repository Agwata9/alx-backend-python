#!/usr/bin/env python3
"""async_comprehension"""


import asyncio

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """Run time for four parallel comprehensions"""

    start_time = asyncio.get_running_loop().time()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
    )
    end_time = asyncio.get_running_loop().time()
    return end_time - start_time
