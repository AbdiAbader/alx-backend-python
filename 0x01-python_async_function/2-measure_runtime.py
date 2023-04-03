#!/usr/bin/env python3
""" Measure the runtime """

import asyncio
import time
import random
from typing import List

wait_n = __import__('2-measure_runtime').wait_n


def measure_time(n: int, max_delay: int) -> float:
    start_time = time.monotonic()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(wait_n(n, max_delay))
    end_time = time.monotonic()
    total_time = end_time - start_time
    return total_time / n
