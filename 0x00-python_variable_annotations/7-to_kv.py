#!/usr/bin/env python3
"""
    Mixed Tuple
"""
from typing import Union, Tuple

def to_kiv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
        Args:
            k: String
            v: Union: Can be int or float
        Return:
            Tuple with string and int or float
    """


    return k, float(v ** 2)
