#!/usr/bin/env python3
"""Module defines `sum_list` function"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Return summ of elements in `input_list`"""
    return sum(elem for elem in input_list)
