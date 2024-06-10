#!/usr/bin/env python3
"""
Task: 1, make concurrent co-routines
"""
import typing
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> typing.List[float]:
    """
    Task: 1, make concurrent co-routines
    args: n: int, max_delay: int.
    return: typing.List of floats.
    """
    output: typing.List = []
    for _ in range(n):
        output.append(await wait_random(max_delay))
    return output
