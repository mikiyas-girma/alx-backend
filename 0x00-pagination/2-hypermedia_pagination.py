#!/usr/bin/env python3
"""dataset pagination module"""
from typing import Tuple, Dict
import csv
from typing import List
import math


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """returns page index range from a given
    page and page size
    """
    initial = (page - 1) * page_size
    last = initial + page_size
    return (initial, last)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """takes two arguments and returns the appropriate
        page of the dataset
        """
        assert isinstance(page, int)
        assert isinstance(page_size, int)
        assert page > 0
        assert page_size > 0

        initial, last = index_range(page, page_size)
        dataset = self.dataset()
        if initial > len(dataset):
            return []

        return dataset[initial:last]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """returns a dictionary of the ff key value pairs"""
        page_data = self.get_page(page, page_size)
        initial, last = index_range(page, page_size)
        total_pages = math.ceil(len(self.__dataset) / page_size)
        next_page = page + 1 if last < len(self.__dataset) else None
        prev_page = page - 1 if initial > 0 else None

        page_info = {
            'page_size': len(page_data),
            'page': page,
            'data': page_data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages,
        }

        return page_info
