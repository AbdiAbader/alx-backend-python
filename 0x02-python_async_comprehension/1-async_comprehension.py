#!/usr/bin/env python3
""" Async Comprehensions """
import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collect 10 random numbers using an async comprehension over async_generator,
    then return the 10 random numbers.
    """
    random_numbers = [x async for x in async_generator()][:10]
    return random_numbers
