#!/usr/bin/env python3
""" Basic async syntax """

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ wait for randomly and returns """
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
