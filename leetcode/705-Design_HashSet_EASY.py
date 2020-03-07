# 705-Design_HashSet_EASY.py

# Design a HashSet without using any built-in hash table libraries.

# To be specific, your design should include these functions:

# add(value): Insert a value into the HashSet.
# contains(value) : Return whether the value exists in the HashSet or not.
# remove(value): Remove a value in the HashSet. If the value does not exist in the HashSet, do nothing.

# Example:

# MyHashSet hashSet = new MyHashSet();
# hashSet.add(1);
# hashSet.add(2);
# hashSet.contains(1);    // returns true
# hashSet.contains(3);    // returns false (not found)
# hashSet.add(2);
# hashSet.contains(2);    // returns true
# hashSet.remove(2);
# hashSet.contains(2);    // returns false (already removed)

# Note:

# All values will be in the range of [0, 1000000].
# The number of operations will be in the range of [1, 10000].
# Please do not use the built-in HashSet library.

# Start: 3:27pm End: 3:44... Still can't figure out why this is so slow
# Runtime: 2180 ms, faster than 5.02% of Python3 online submissions for Design HashSet.
# Memory Usage: 16.8 MB, less than 100.00% of Python3 online submissions for Design HashSet.

# Assumptions
# see Note above

# Approach
# initialize array of 1000 empty lists and hash function of val % 1000
# append a new element to it's appropriate list, getting index by hash func
# remove by checking contains and then popping at index if contains

# Edge Cases
# remove when not exists


class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashmod = 1000
        self.table = [[None]] * self.hashmod


    def add(self, key: int) -> None:
        # only add if not already in hashset
        if not self.contains(key):
            index = key % self.hashmod
            self.table[index].append(key)


    def remove(self, key: int) -> None:
        # only remove if already in hashset
        if self.contains(key):
            index = key % self.hashmod
            self.table[index].remove(key)


    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        index = key % self.hashmod
        return key in self.table[index]



# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)


if __name__ == '__main__':
    # run example

    hashSet = MyHashSet()
    hashSet.add(1)
    hashSet.add(2)
    print(hashSet.contains(1))
    print(hashSet.contains(3))
    hashSet.add(2)
    print(hashSet.contains(2))
    hashSet.remove(2)
    print(hashSet.contains(2))

