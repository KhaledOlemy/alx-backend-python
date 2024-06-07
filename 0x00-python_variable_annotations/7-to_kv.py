#!/usr/bin/env python3
"""
xx
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    kv to kv^2
    """
    return (k, float(v**2))
