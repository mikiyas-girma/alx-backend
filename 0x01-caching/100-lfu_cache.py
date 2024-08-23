#!/usr/bin/env python3
""" Least Frequently Used caching module.
"""
from base_caching import BaseCaching
from collections import OrderedDict


class LFUCache(BaseCaching):
    """Least Frequently Used caching system.
    """
    def __init__(self):
        """Initializes the class instance.
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Adds an item in the cache.
        """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                lfu_key = min(self.cache_data, key=lambda x: x[1])
                self.cache_data.pop(lfu_key)
                print("DISCARD:", lfu_key)
            self.cache_data[key] = 1
        else:
            self.cache_data[key] += 1

    def get(self, key):
        """Retrieves an item by key
        """
        if key is not None and key in self.cache_data:
            self.cache_data[key] += 1
        return self.cache_data.get(key, None)
