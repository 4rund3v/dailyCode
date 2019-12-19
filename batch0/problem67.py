"""
This problem was asked by Google.

Implement an LFU (Least Frequently Used) cache. It should be able to be initialized with a cache size n, and contain the following methods:

set(key, value): sets key to value. If there are already n items in the cache and we are adding a new item, then it should also remove the least frequently used item. If there is a tie, then the least recently used key should be removed.
get(key): gets the value at key. If no such key exists, return null.
Each operation should run in O(1) time.
"""


from collections import OrderedDict
from collections.abc import MutableMapping

class LruCache(MutableMapping):

    def __init__(self, max_size=10, *args, **kwargs):
        self.max_size = max_size
        self.store = OrderedDict()
        self.update(dict(*args, **kwargs))

    def __getitem__(self, key):
        # Move the key to the end of the cache
        try:
            self.store[key] = self.store.pop(key)
            return self.store[key]
        except KeyError:
            if not hasattr(self, '__missing__'):
                raise
            else:
                return self.__missing__(key)

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def __setitem__(self, key, value):
        try:
            self.store.pop(key)
        except KeyError:
            # We just want to move it to the back, so ignore it
            pass

        self.store[key] = value

        while len(self) > self.max_size:
            self.store.popitem(last=False)

    def __delitem__(self, key):
        del self.store[key]

    def __iter__(self):
        return iter(self.store)

    def __len__(self):
        return len(self.store)

