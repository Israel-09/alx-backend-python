#!/usr/bin/env python3
"""
sum of list elements
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    sums up the list
    """
    total: float = 0

    for num in input_list:
        total += num
    return total
