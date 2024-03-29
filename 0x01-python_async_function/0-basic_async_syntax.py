#!/usr/bin/env python3
"""
asyncio python tutorial
"""
import asyncio
from random import uniform


async def wait_random(max_delay: int = 10) -> float:
    """
    wait randomly for up to max_delay
    """
    delay = uniform(0, max_delay)

    await asyncio.sleep(delay)
    return delay
