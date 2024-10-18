#!/usr/bin/env python3
from typing import List

"""
This module provides a function to sum a list of floating-point numbers.
"""

def sum_list(input_list: List[float]) -> float:
    """
    Return the sum of a list of floats.

    Args:
        input_list (List[float]): A list of floating-point numbers.

    Returns:
        float: The sum of the list elements.
    """
    return sum(input_list)
