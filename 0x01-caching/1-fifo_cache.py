#!/usr/bin/env python3
""" FIFO cache replacement policy module"""

from base_caching import BaseCaching
from collections import OrderedDict


class FIFOCache(BaseCaching):
    """ FIFO cache replacement system """

    def __init__(self):
        """ Initializes class """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Add an item in the cache """
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                first = next(iter(self.cache_data))
                del self.cache_data[first]
                print("DISCARD: {}".format(first))

    def get(self, key):
        """ Get an item by key """
        return self.cache_data.get(key, None)
