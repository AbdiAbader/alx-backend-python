#!/usr/bin/env python3
""" Measure the runtime """

import asyncio
import time
import random
from typing import List

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ Measure the runtime """
    start: float = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end: float = time.perf_counter()
    return (end - start) / n
