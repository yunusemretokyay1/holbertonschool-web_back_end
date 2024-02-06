#!/usr/bin/env python3
"""async comprehension module
"""
import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator



async def async_comprehension() -> List[float]:
    """createe a list ith 10 number
    returns: List [float]:a list with result of sync generator method
    """
    return [n async for n in async_generator()]