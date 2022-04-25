#!/usr/bin/env python3
"""Module defines `measure_runtime` coroutine"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Return time duration of 4 coroutine calls"""
    started = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    ended = time.perf_counter()
    return ended - started
