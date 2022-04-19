#!/usr/bin/env python3
"""Module defines `element_length` function"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return a list of tuples based on `lst` parameter"""
    return [(i, len(i)) for i in lst]
