#!/usr/bin/env python3
"""
A regular function, task_wait_random, that takes an integer max_delay
 and returns a asyncio.Task
"""

import asyncio
import time

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int = 0) -> asyncio.Task:
    """
    Return asyncio Task and takes max_delay as an argument
    """
    todo = asyncio.create_task(wait_random(max_delay))
    return todo
