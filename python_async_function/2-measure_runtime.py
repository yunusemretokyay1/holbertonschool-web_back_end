#!/usr/bin/env python3
"""measure time module
"""
import asyncio
import random
from time import perf_counter

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
     ''' returns the elapsed time'''
    start_task = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_task = time.time()
    total_time: float = end_task - start_task
    return total_time / n
