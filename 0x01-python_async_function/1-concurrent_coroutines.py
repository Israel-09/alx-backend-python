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
    batch = asyncio.gather(*(wait_random(max_delay) for i in range(n)))
    delays = await batch

    return delays
