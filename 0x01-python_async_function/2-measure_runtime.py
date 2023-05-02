#!/usr/bin/env python3
""" Comprehension project """
import asyncio
import time
from typing import Coroutine

async_comprehension = __import__('1-async_comprehension').async_comprehension


def task_wait_random(max_delay: int) -> asyncio.Task:
    coro = wait_random(max_delay)
    task = asyncio.create_task(coro)
    return task
