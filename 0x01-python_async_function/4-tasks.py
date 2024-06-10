#!/usr/bin/env python3
"""
Task: 4, 
"""
import typing
wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> typing.List[float]:
    """
    Task: 1, make co-routines, handle when task_wait_random is called
    args: n: int, max_delay: int.
    return: typing.List of floats.
    """
    output: typing.List = []
    for _ in range(n):
        output.append(await wait_random(max_delay))
    return output
