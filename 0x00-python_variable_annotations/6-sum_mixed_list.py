#!/usr/bin/env python3
""" Mixed List"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ return mixed list sum"""
    total: float = 0
    for i in range(0, len(mxd_lst)):
        total += mxd_lst[i]
    return total
