#!/usr/bin/env python3
"""Callable Function"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ make multiplier"""
    def multiplier_fn(x: float) -> float:
        """multiplier_fn"""
        return x * multiplier
    return multiplier_fn
