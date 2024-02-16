#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict

class Server:
    """
    Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """
        Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset
    def indexed_dataset(self) -> Dict[int, List]:
        """
        Dataset from 'DATA_FILE',
        cached as a dictionary of the rows' indexes
        and their contents,

        so that even if a row is deleted,
        the other rows don't offset.
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset
    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Returns a dictionary:
            """
        INDEXED_DATASET: Dict[int, List] = self.indexed_dataset()

        PAGE_DATA: List[List] = [
            INDEXED_DATASET[i]
            for i in range(index, index + page_size)
            if i in INDEXED_DATASET
        ]

        return {
            "index": index,
            "next_index": index + page_size,
            "page_size": len(PAGE_DATA),
            "data": PAGE_DATA
        }