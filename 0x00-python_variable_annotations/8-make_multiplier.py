#!/usr/bin/env python3
"""
return a callable object
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """make mulitiplier
    """
    return lambda num: num * multiplier
