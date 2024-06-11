#!/usr/bin/env python3
"""
Task: 4, make co-routines, handle when task_wait_random is called
"""
import typing
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> typing.List[float]:
    """
    Task: 4, make co-routines, handle when task_wait_random is called
    args: n: int, max_delay: int.
    return: typing.List of floats.
    """
    output: typing.List = []
    for _ in range(n):
        output.append(await task_wait_random(max_delay))
    return sorted(output)
