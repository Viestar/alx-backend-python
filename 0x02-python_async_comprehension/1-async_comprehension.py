#!/usr/bin/env python3
"""
A coroutine that collects 10 random numbers using async comprehension over
the previous async_generator, then return the 10 random numbers
"""
import asyncio
import random
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    collects 10 random numbers using async comprehension, imported coroutine,
      and return the random numbers
    """
    result = [i async for i in async_generator()]
    return result
