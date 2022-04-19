#!/usr/bin/env python3
"""Module defines `sum_mixed_list` function"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Return sum of all elements in `mxd_lst`"""
    return sum(elem for elem in mxd_lst)
