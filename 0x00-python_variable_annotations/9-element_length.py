#!/usr/bin/env python3
"""
fix function | add annotations
"""
from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    add annotations to function
    """
    return [(i, len(i)) for i in lst]
