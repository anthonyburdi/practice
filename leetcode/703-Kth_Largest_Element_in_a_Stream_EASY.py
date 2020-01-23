# 703-Kth_Largest_Element_in_a_Stream_EASY.py

# https://leetcode.com/problems/kth-largest-element-in-a-stream/

# Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

# Your KthLargest class will have a constructor which accepts an integer k and an integer array nums, which contains initial elements from the stream. For each call to the method KthLargest.add, return the element representing the kth largest element in the stream.

# Example:

# int k = 3;
# int[] arr = [4,5,8,2];
# KthLargest kthLargest = new KthLargest(3, arr);
# kthLargest.add(3);   // returns 4
# kthLargest.add(5);   // returns 5
# kthLargest.add(10);  // returns 5
# kthLargest.add(9);   // returns 8
# kthLargest.add(4);   // returns 8
# Note:
# You may assume that nums' length ≥ k-1 and k ≥ 1.

from typing import List

class KthLargest:

    def __init__(self, k: int, nums: List[int]):

        self.k = k
        self.nums = nums
        # Initialize with sorted array of the largest elements of nums:
        self.kth_largest_elements = sorted(nums)[-k:]


    def add(self, val: int) -> int:

        # check if bigger than kth largest, or if kth largest isn't full
        if (
            (len(self.kth_largest_elements) < self.k) or
            (val > self.kth_largest_elements[0])
        ):
            self.insert_and_sort(val)

        # return minimum element. safe bc we always have one element by
        # this point even if starting with nums = []
        return self.kth_largest_elements[0]


    def insert_and_sort(self, val: int) -> None:
        """Insert single element into list and re-sort the list."""

        # add the value if an empty list:
        if self.kth_largest_elements == []:
            self.kth_largest_elements.append(val)
            return

        # O(NlogN) insert (32 ms with example)

        # replace minimum with added element if larger
        if (len(self.kth_largest_elements) < self.k):
            self.kth_largest_elements.append(val)
        else:
            self.kth_largest_elements[0] = val

        # re-sort self.kth_largest_elements
        self.kth_largest_elements = sorted(self.kth_largest_elements)

        # # O(N) insert (24 ms with example)
        # # Too slow for leetcode

        # # Insert before element larger or equal to val

        # # Remove the smallest element or add a new smallest element
        # if (len(self.kth_largest_elements) < self.k):
        #     self.kth_largest_elements = [None] + self.kth_largest_elements
        # else:
        #     self.kth_largest_elements[0] = None

        # i = 0
        # while i < len(self.kth_largest_elements) - 1:
        #     # check if the next element is equal or larger, if so insert in i-1
        #     if self.kth_largest_elements[i + 1] >= val:
        #         self.kth_largest_elements[i] = val
        #         break
        #     # if not, then swap the next element and the previous
        #     # to move the empty space down
        #     else:
        #         self.kth_largest_elements[i] = self.kth_largest_elements[i + 1]
        #         self.kth_largest_elements[i + 1] = None

        #     i += 1

        # # if largest element, insert at the end
        # if self.kth_largest_elements[-1] == None:
        #     self.kth_largest_elements[-1] = val



# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)


# Assumptions
# elements are numeric
# k elements can fit on a single machine or the api for multi-machine
# lists is the same as on a single machine

# Approach
# Keep a sorted array of the kth largest elements so far.
# initialize with sorted array of the largest elements of nums.
# Keep the minimum element in the largest elements
# If the new element is larger than the minimum, replace
# the minimum with it and re-sort the largest elements.
# Return the minimum element on each add.

# Complexity
# Time
# Each insert we have to check whether it is larger than the smallest
# element (the kth largest). If it is we need to insert and re-sort
# the largest elements. Everything other than the re-sort is O(1) and
# the re-sort can be done in O(NlogN) time. However if we start with
# a sorted list, we are only inserting one element. We can do that in O(N)
# time by checking each value and inserting before any that are larger.
# Space
# O(k) since we store the kth largest elements and a few variables

# Potential improvements
# Maybe instead of sorting on each insert of the kth list we can iterate
# through it until we find a larger element than the one to be inserted
# and then insert it before that element.

# This could also be done with a min heap of size k
# Also the insertion can be done with a binary search type algorithm to
# find where to insert


#  Edge cases
# I can't think of any. All are covered in the example note


# Examples:

# Given
# ["KthLargest","add","add","add","add","add"]
# [[3,[4,5,8,2]],[3],[5],[10],[9],[4]]

# list index out of range
# ["KthLargest","add","add","add","add","add"]
# [[1,[]],[-3],[-2],[-4],[0],[4]]

# Wrong Answer
# Input
# ["KthLargest","add","add","add","add","add"]
# [[2,[0]],[-1],[1],[-2],[-4],[3]]
# Output
# [null,-1,1,-2,-4,3]
# Expected
# [null,-1,0,0,0,1]

# ["KthLargest","add","add","add","add","add"]
# [[3,[4,5,8,2]],[3],[5],[10],[9],[4]]
# ["KthLargest","add","add","add","add","add"]
# [[1,[]],[-3],[-2],[-4],[0],[4]]
# ["KthLargest","add","add","add","add","add"]
# [[2,[0]],[-1],[1],[-2],[-4],[3]]









