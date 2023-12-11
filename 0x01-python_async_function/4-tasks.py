#!/usr/bin/env python3
"""
Contains a new function task_wait_n spawns todos n times with a
given delay between each function call
"""

import asyncio
from asyncio.tasks import Task
from typing import List

task_wait_random = __import__('3-todos').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Returns a list of delays and takes n and max_delay
    """
    todos = [task_wait_random(max_delay) for _ in range(n)]
    return [await task for task in asyncio.as_completed(todos)]
