#!/usr/bin/env python3
"""Module defines async `wait_random` function"""
import asyncio
from random import uniform


async def wait_random(max_delay: int = 10) -> float:
    """Waits for a max of `max_delay` seconds and returns"""
    i = uniform(0, max_delay)
    await asyncio.sleep(i)
    return i
