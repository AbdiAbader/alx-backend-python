#!/usr/bin/env python3
""" Basic async syntax """

from asyncio import sleep
import random


async def wait_random(max_delay: int = 10) -> float:
    """ wait for randomly and returns """
    delay = random.uniform(0, max_delay)
    await sleep(delay)
    return delay
