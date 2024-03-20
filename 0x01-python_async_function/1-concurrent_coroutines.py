#!/usr/bin/env python3
"""
asyncio module tutorial
"""
import asyncio
from typing import List


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    return an array of delay
    """
    wait_random = __import__('0-basic_async_syntax').wait_random

    tasks = [wait_random(max_delay) for _ in range(n)]
    result = []
    for task in asyncio.as_completed(tasks):
        result.append(await task)

    return result
