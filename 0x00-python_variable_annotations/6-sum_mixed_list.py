#!/usr/bin/env python3
"""
sum mixed list
"""
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    sums up a list of float and integer
    """
    sum: float = 0
    for num in mxd_lst:
        sum += num
    return sum
