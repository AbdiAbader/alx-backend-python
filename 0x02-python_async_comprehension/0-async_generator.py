#!/usr/bin/env python3
""" Aync Generator"""

import asyncio
import random


async def async_generator() -> float:
    """ Async Generator"""
    for _ in range(10):
        yield random.uniform(0, 10)
        await asyncio.sleep(1)
