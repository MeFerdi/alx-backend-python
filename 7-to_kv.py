#!/usr/bin/env python3
from typing import Union, Tuple

"""
This module provides a function that returns a tuple
with a string and the square of a number.
"""

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Return a tuple with the string k and the square of v.

    Args:
        k (str): A string.
        v (Union[int, float]): A number, either int or float.

    Returns:
        Tuple[str, float]: A tuple where the first element is the string k,
                           and the second element is the square of v as a float.
    """
    return (k, float(v ** 2))
