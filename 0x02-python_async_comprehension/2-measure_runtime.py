#!/usr/bin/env python3

import asyncio
from time import perf_counter

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    async_comprehension
    """
    before = perf_counter()

    result = await asyncio.gather(*(async_comprehension() for _ in range(4)))

    return perf_counter() - before
