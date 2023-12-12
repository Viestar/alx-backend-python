#!/usr/bin/env python3
"""
A coroutine, async_generator, with no arguments looping 10 times, each time
 asynchronously wait 1 second, then yield a random number between 0 and 10.
"""
import asyncio
from typing import Generator
import random


async def async_generator() -> Generator[float, None, None]:
    """
    Each time asynchronously wait 1 second, then
    yield a random number, async generator loops x10
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
