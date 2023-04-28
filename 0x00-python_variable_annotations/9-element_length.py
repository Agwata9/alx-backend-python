#!/usr/bin/env python3
"""
   duck type an iterable object
"""

from typing import Iterable, Sequence, List, Tuple

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Given a list of sequences, return a list of tuples that contain the
    original element and its length.

    Args:
    lst (Iterable[Sequence]): An iterable of sequences.

    Returns:
    List[Tuple[Sequence, int]]: A list of tuples containing each element
    of the input list and its length.
    """
    return [(i, len(i)) for i in lst]
