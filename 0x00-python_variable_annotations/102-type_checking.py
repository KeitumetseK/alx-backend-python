#!/usr/bin/env python3
"""
This module provides a function to zoom in on elements of a tuple by repeating each element.
"""
from typing import List, Tuple, Union

def zoom_array(lst: Tuple[Union[int, float], ...], factor: int = 2) -> List[Union[int, float]]:
    """
    Zooms in on the elements of a tuple by repeating each element a specified number of times.

    Args:
        lst (Tuple[Union[int, float], ...]): The input tuple containing integers or floats.
        factor (int, optional): The factor by which to repeat each element. Defaults to 2.

    Returns:
        List[Union[int, float]]: A list where each element of the input tuple is repeated.
    """
    zoomed_in: List[Union[int, float]] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)
zoom_3x = zoom_array(array, 3)

print(zoom_2x)
print(zoom_3x)

