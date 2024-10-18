#!/usr/bin/env python3
from typing import List, Union

"""
This module provides a function to sum a list of mixed integers and floats.
"""

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Return the sum of a list containing both integers and floats.

    Args:
        mxd_lst (List[Union[int, float]]): A list containing integers and floats.

    Returns:
        float: The sum of the list elements as a float.
    """
    return sum(mxd_lst)
