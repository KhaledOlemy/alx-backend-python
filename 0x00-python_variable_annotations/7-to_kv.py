#!/usr/bin/env python3
"""
kv from (str, (int|float)) to (str, float)
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    kv to kv^2
    """
    return (k, v**2)
