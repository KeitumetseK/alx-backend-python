#!/usr/bin/env python3
"""
This module provides a basic asynchronous coroutine for waiting a random delay.
"""

import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    """
    Waits for a random delay between 0 and max_delay seconds and returns the delay.

    Args:
        max_delay (int): The maximum delay in seconds (default is 10).

    Returns:
        float: The random delay in seconds.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

