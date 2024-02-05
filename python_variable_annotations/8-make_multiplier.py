#!/usr/bin/env python3
"""
make_multiplier 
"""
from typing import Callable


def make_multiplier(multipler: float) -> Callable[[float], float]:
    """
    make_multipler
    
    Args multipler (float): number
    
    Returns: Callable[[float],float]: [description]
    """
    return lambda x: x * multipler
