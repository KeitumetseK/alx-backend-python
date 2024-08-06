#!/usr/bin/env python3
"""
This module provides a coroutine for waiting multiple random delays concurrently.
"""

import asyncio
from typing import List
import importlib

wait_random = importlib.import_module('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times with the specified max_delay and returns a list of delays.

    Args:
        n (int): The number of times to spawn wait_random.
        max_delay (int): The maximum delay in seconds.

    Returns:
        List[float]: A list of delays in ascending order.
    """
    delays = [await wait_random(max_delay) for _ in range(n)]
    return sorted(delays)

