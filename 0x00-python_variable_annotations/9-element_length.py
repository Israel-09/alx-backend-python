#!/usr/bin/env python3
"""
element length
"""
from typing import Iterable, Tuple, List, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    get the length of every list element in a list
    """
    return [(i, len(i)) for i in lst]
