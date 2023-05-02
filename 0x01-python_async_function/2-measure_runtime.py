#!/usr/bin/env python3

import time
from typing import List


def wait_n(n: int, max_delay: int) -> List[float]:
    """Generate n random delays of up to max_delay seconds."""
    delays = [random.uniform(0, max_delay) for _ in range(n)]
    return sorted(delays)


def measure_time(n: int, max_delay: int) -> float:
    """Measure the average execution time of wait_n function."""
    start = time.time()
    wait_n(n, max_delay)
    end = time.time()
    total_time = end - start
    return total_time / n

