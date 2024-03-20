#!/usr/bin/env python3
"""
async_comprehension
"""

import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[int]:
    """
    async comprehension
    """

    result = []

    async for num in async_generator():
        result.append(num)

    return result
