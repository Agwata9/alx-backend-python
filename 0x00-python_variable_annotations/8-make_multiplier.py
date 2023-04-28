#!/usr/bin/env python3
"""
    Callable function
"""

from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Return a function that multiplies a float by a given multiplier.

    Args:
    multiplier (float): A floating-point number.

    Returns:
    Callable[[float], float]: A function that multiplies a float by `multiplier`.
    """
    def multiplier_fn(num: float) -> float:
        return num * multiplier
    return multiplier_fn
