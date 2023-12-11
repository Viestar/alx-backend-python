#!/usr/bin/env python3
"""
This module starts From the previous file, import wait_n into
2-measure_runtime.py. Create a measure_time function with
 integers n and max_delay as arguments that measures the total
   execution time for wait_n(n, max_delay), and returns total_time
    / n. Your function should return a float.

Use the time module to measure an approximate time_elapsed time..
"""

import asyncio
import random
import time
from typing import List


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int = 10) -> float:
    """
    returns total_time / n and takes n and max_delay as input to
    measure execution time are
    """
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    time_elapsed = time.perf_counter() - start_time
    return time_elapsed / n
