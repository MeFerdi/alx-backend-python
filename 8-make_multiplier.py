#!/usr/bin/env python3
from typing import Callable

"""
This module provides a function that returns a multiplier function.
"""

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create a function that multiplies a float by a given multiplier.

    Args:
        multiplier (float): The multiplier to use.

    Returns:
        Callable[[float], float]: A function that takes a float and returns
                                   the product of the float and the multiplier.
    """
    def multiply(n: float) -> float:
        return n * multiplier
    return multiply
