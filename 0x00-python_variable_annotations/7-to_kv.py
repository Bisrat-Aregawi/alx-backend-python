#!/usr/bin/env python3
"""Module defines `to_kv` function"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Function returns a tupple of `k` and `v`"""
    return k, v ** 2
