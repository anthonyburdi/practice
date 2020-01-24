# 146-LRU_Cache_MEDIUM.py

# https://leetcode.com/problems/lru-cache/

# Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

# get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
# put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

# The cache is initialized with a positive capacity.

# Follow up:
# Could you do both operations in O(1) time complexity?

# Example:

# LRUCache cache = new LRUCache( 2 /* capacity */ );

# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // returns 1
# cache.put(3, 3);    // evicts key 2
# cache.get(2);       // returns -1 (not found)
# cache.put(4, 4);    // evicts key 1
# cache.get(1);       // returns -1 (not found)
# cache.get(3);       // returns 3
# cache.get(4);       // returns 4


# Approach etc in notebook
# What to do with overwrite?

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.stack = []
        self.value_store = {}


    def get(self, key: int) -> int:
        value = self.value_store.get(key, -1)
        if value == -1:
            return value
        else:
            key = self.stack.pop(self.stack.index(key)) # O(capacity)
            self.stack.append(key)
            return value


    def put(self, key: int, value: int) -> None:

        # if key already exists, just modify
        if key in self.value_store:
            self.value_store[key] = value
            # move to top
            self.get(key)
            return

        at_capacity = len(self.stack) >= self.capacity

        if at_capacity:
            evicted = self.stack.pop(0) # O(capacity)
            self.value_store.pop(evicted)

        self.stack.append(key)
        self.value_store[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# Modification case
# KeyError: 2
# ["LRUCache","put","put","get","put","put","get"]
# [[2],[2,1],[2,2],[2],[1,1],[4,1],[2]]


# Example 1
# ["LRUCache","put","put","get","put","get","put","get","get","get"]
# [[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]

