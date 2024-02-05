#!/usr/bin/env python3
"""
Has one function named 'sum_mixed_list'.

'sum_mixed_list' takes one argument 'mxd_lst',
which should be a list of ints or floats,
and returns their sum, which should be a float.

Uses 'typing' and python type annotations
to specify that the input for 'sum_mixed_list'
is a list of ints/floats, and that
'sum_mixed_list' returns a float.
"""

from typing import List, Union

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculates the sum of integers and floats in the input list.

    Parameters:
    - mxd_lst (List[Union[int, float]]): A list containing integers and floats.

    Returns:
    float: The sum of the elements in the input list.
    """
    return sum(mxd_lst)


