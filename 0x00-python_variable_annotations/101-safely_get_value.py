#!/usr/bin/env python3
"""
TypeVar | involved type annotations
"""
from typing import Mapping, Any, Union, TypeVar

T = TypeVar('T')
output = Union[Any, T]
Def = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default: Def = None) -> output:
    """
    TypeVar annotations
    """
    if key in dct:
        return dct[key]
    else:
        return default
