#!/usr/bin/env python3
""" 4-tasks.py """

import asyncio
import random

wait_n = __import__('1-concurrent_coroutines').wait_n


def task_wait_random(n: int, max_delay: int) -> asyncio.Task:
    """ Returns an asyncio.Task """
    return asyncio.create_task(wait_n(n, max_delay))
