#!/usr/bin/env python3
"""
0-async_generator.py
"""
from random import uniform
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    generated 10 random floats
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield uniform(0, 10)
