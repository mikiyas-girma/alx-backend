#!/usr/bin/env python3
""" LIFO cache replacement policy module"""

from base_caching import BaseCaching
from collections import OrderedDict


class LIFOCache(BaseCaching):
    """ LIFO cache replacement system """

    def __init__(self):
        """ Initializes class """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Add an item in the cache """
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                last = next(reversed(self.cache_data))
                del self.cache_data[last]
                print("DISCARD: {}".format(last))

    def get(self, key):
        """ Get an item by key """
        return self.cache_data.get(key, None)
