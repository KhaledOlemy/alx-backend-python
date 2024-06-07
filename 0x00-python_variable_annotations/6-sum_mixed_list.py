#!/usr/bin/env python3
"""
sum_mixed_list float and ints to float
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """sums arrays of floats"""
    return sum(mxd_lst)
