#!/usr/bin/env python3
""" Async Comprehensions """
import asyncio
from typing import List

import random

async def async_comprehension() -> List[float]:
    return [random.random() * 10 for _ in range(10)]


async def measure_runtime() -> float:
    start_time = asyncio.get_running_loop().time()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
    )
    end_time = asyncio.get_running_loop().time()
    return end_time - start_time
