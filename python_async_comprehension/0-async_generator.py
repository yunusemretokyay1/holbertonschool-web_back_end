#!/usr/bin/env python3
"""
async generator module
"""
import asyncio
import random
from typing import Generator

async def async_generator() -> Generator[float, None, None]:
    '''
        Loops 10 times with a 1 sec wait

    '''
    for integer in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
        
