#!/usr/bin/python3
"""Simple helper"""


def index_range(page: int, page_size: int) -> tuple[int, int]:
    end = page_size * page
    return(end-page_size,end)