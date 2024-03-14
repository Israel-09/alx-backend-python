#!/usr/bin/env python3
"""
complex type annotation module
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    returns a tupple with a string and int/float
    """
    return k, pow(v, 2)
