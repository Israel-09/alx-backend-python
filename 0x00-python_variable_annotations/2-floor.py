#!/usr/bin/env python3
"""
math function module
"""

def floor(n: float) -> int:
    """
    returns the floored value of a float
    """
    from math import floor as builtin_floor
    return builtin_floor(n)
