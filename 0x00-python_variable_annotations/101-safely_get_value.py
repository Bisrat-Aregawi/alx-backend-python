#!/usr/bin/env python3
"""Module defines `safely_get_value` function"""
from typing import Mapping, TypeVar, Union, Any


T = TypeVar('T')


def safely_get_value(
    dct: Mapping,
    key: Any,
    default: Union[T, None] = None
) -> Union[Any, T]:
    """Return Value of `dct` @ `key` or the default parameter"""
    if key in dct:
        return dct[key]
    else:
        return default
