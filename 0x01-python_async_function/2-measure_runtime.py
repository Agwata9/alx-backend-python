#!/usr/bin/env python3
"""Measure the runtime module"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Generate n random delays of up to max_delay seconds."""

    initial = time.time()

    asyncio.run(wait_n(n, max_delay))

    end = time.time()

    return (end - initial) / n
