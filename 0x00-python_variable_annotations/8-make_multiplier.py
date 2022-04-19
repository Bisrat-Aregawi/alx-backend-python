#!/usr/bin/env python3
"""Module defines `make_multiplier` function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function"""
    def fun(flt_num: float) -> float:
        """Return the multiplication of `multiplier` and flt_num"""
        return flt_num * multiplier
    return fun
