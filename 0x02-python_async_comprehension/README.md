# Python Async Comprehensions

This repository contains three tasks demonstrating the use of asynchronous comprehensions and coroutines in Python.

## Tasks

### 0. Async Generator
- **File:** `0_async_generator.py`
- **Description:** This module defines `async_generator`, a coroutine that yields a random number between 0 and 10 after waiting for 1 second, repeated 10 times.

### 1. Async Comprehensions
- **File:** `1_async_comprehension.py`
- **Description:** This module defines `async_comprehension`, a coroutine that collects 10 random numbers from `async_generator` using an async comprehension.

### 2. Run time for four parallel comprehensions
- **File:** `2_measure_runtime.py`
- **Description:** This module defines `measure_runtime`, a coroutine that executes `async_comprehension` four times in parallel using `asyncio.gather` and measures the total runtime.

## How to Run
1. Ensure you have Python 3.7 installed.
2. Clone this repository.
3. Run the provided `main.py` files for each task to see the output.

```bash
$ ./0-main.py
$ ./1-main.py
$ ./2-main.py

