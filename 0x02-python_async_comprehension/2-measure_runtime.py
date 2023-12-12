#!/usr/bin/env python3
"""
A coroutine that will execute async_comprehesion four times in parallel using
 asyncio.gather. measure_runtime returns the total runtime.
"""
import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ Returns the total runtime for 4 parallel asynchronous comprehension """
    start = time.perf_counter()
    result = await asyncio.gather(*(async_comprehension() for _ in range(4)))
    total = time.perf_counter() - start
    return total
