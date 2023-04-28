#!/usr/bin/env python3
"""
    List of floats annotations
"""

from typing import List

def sum_list(input_list: List[float]) -> float:
    """

    Args:
    input_list (List[float]): A list of floating-point numbers.

    Returns:
    float: The sum of the elements in `input_list`.
    """
    return sum(input_list)
