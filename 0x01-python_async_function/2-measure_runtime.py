#!/usr/bin/env python3
"""
asyncio module tutorial
"""
from time import perf_counter
import asyncio


def measure_time(n: int, max_delay: int) -> float:
    """
    measure total time ti run asynchronoun program
    """
    wait_n = __import__("1-concurrent_coroutines").wait_n
    before_run = perf_counter()
    asyncio.run(wait_n(n, max_delay))
    total_time = perf_counter() - before_run
    return total_time / n
