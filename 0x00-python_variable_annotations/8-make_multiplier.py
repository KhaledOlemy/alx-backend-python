#!/usr/bin/env python3
"""
take float and squares it
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Callable function float
    """
    return lambda o: o * multiplier
