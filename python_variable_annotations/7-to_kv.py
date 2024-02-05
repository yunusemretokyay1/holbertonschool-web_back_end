#!/usr/bin/env python3

from typing import List, Union, Tuple

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Converts the input value 'v' to its square and returns a tuple.

    Parameters:
    - k (str): The key value.
    - v (Union[int, float]): The value which can be an integer or a float.

    Returns:
    Tuple[str, float]: A tuple containing the key 'k' and the square of 'v' as a float.
    """
    return k, float(v ** 2)

