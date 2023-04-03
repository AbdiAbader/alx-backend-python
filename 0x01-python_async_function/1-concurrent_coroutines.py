#!/usr/bin/env python3
""" Concurrent coroutines """
import asyncio
import random
from typing import List
import heapq

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    delays = []
    for i in range(n):
        delay = await wait_random(max_delay)
        heapq.heappush(delays, delay)
    return [heapq.heappop(delays) for _ in range(n)]
