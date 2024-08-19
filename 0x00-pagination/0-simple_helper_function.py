#!/usr/bin/env python3
"""simple helper function module"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """returns page index range from a given
    page and page size
    """
    initial = (page - 1) * page_size
    last = initial + page_size
    return (initial, last)
