#!/usr/bin/env python3
"""
Task: 0, wait a random time between 0 and the max_delay
"""
import asyncio
import random


async def wait_random(max_delay=10):
    """
    Wait a random time between 0 and the max_delay
    Then return the delay you took
    """
    randWaitTime = random.random() * max_delay
    await asyncio.sleep(randWaitTime)
    return randWaitTime
