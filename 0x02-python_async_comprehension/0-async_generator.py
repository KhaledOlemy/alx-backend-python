#!/usr/bin/env python3
"""
Task: 0,
"""
import asyncio
import typing as ty
import random


async def async_generator() -> ty.Generator[float, None, None]:  # type: ignore
    """
    Task: 0, The coroutine will loop 10 times,
    each time asynchronously wait 1 second, then
    yield a random number between 0 and 10
    return type should be:
    typing.AsyncGenerator[float, None]
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
