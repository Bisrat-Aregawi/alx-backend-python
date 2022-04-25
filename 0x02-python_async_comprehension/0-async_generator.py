#!/usr/bin/env python3
"""Module defines `async_generator` coroutine"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Yield 10 random numbers"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
