#!/usr/bin/env python3
"""
This module provides a function to get the length of elements in a sequence.
"""
from typing import List, Tuple, Iterable, Sequence

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples with elements and their lengths.

    Args:
        lst (Iterable[Sequence]): The input iterable of sequences.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples where each tuple contains a sequence and its length.
    """
    return [(i, len(i)) for i in lst]

