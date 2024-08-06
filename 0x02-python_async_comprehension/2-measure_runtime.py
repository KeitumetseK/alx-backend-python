#!/usr/bin/env python3
"""Module for measure_runtime coroutine"""

import asyncio
import time
from importlib import import_module

async_comprehension = import_module('1-async_comprehension').async_comprehension

async def measure_runtime() -> float:
    """Measures the runtime of executing async_comprehension four times in parallel"""
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.time() - start_time

