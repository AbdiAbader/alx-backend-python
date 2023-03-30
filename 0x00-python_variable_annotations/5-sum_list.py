#!/usr/bin/env python3
"""" REturn Sum list in float"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """return a sum of inputlist in float"""
    total: float = 0
    for i in range(0, len(input_list)):
        total += input_list[i]
    return total
