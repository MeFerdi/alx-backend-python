#!/usr/bin/env python3
"""
This module provides a function to calculate the floor of a floating-point number.
"""

import math

def floor(n: float) -> int:
    """
    Return the floor of a floating-point number.

    Args:
        n (float): The floating-point number.

    Returns:
        int: The largest integer less than or equal to n.
    """
    return math.floor(n)
