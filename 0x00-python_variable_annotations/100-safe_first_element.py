#!/usr/bin/env python3
"""
    Duck typing sequence Any
"""
from typing import Any, Sequence, Union

def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Given a list, return the first element if it exists, else return None.

    Args:
    lst (Sequence[Any]): A sequence of elements of any type.

    Returns:
    Union[Any, None]: The first element of the input sequence, or None if the
    sequence is empty.
    """
    if lst:
        return lst[0]
    else:
        return None
