#!/usr/bin/env python3
"""
mesure time
"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n

milliseconds = float


def measure_time(n: int, max_delay: int) -> float:
    """
   Measures time of async funcs.

    Args:
        n (int): times
        max_delay (int): dalay max number

    Returns:
        float: total_time
    """
    before: float = time.process_time()
    asyncio.run(wait_n(n, max_delay))
    after: float = time.process_time()

    total_time: float = after - before
    return total_time / n
