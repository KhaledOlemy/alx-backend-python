#!/usr/bin/env python3
"""
Task: 2, measure the runtime
"""
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """compute the average runtime total(delay)/n"""
    ...
    startingTime = time.time()
    asyncio.run(wait_n(n, max_delay))
    endingTime = time.time()
    return (endingTime - startingTime) / n
