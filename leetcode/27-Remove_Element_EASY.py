# 27-Remove_Element_EASY.py

# https://leetcode.com/problems/remove-element/

# Given an array nums and a value val, remove all instances of that value in-place and return the new length.

# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

# The order of elements can be changed. It doesn't matter what you leave beyond the new length.

# Example 1:

# Given nums = [3,2,2,3], val = 3,

# Your function should return length = 2, with the first two elements of nums being 2.

# It doesn't matter what you leave beyond the returned length.
# Example 2:

# Given nums = [0,1,2,2,3,0,4,2], val = 2,

# Your function should return length = 5, with the first five elements of nums containing 0, 1, 3, 0, and 4.

# Note that the order of those five elements can be arbitrary.

# It doesn't matter what values are set beyond the returned length.
# Clarification:

# Confused why the returned value is an integer but your answer is an array?

# Note that the input array is passed in by reference, which means modification to the input array will be known to the caller as well.

# Internally you can think of this:

# // nums is passed in by reference. (i.e., without making a copy)
# int len = removeElement(nums, val);

# // any modification to nums in your function would be known by the caller.
# // using the length returned by your function, it prints the first len elements.
# for (int i = 0; i < len; i++) {
#     print(nums[i]);
# }

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        # Assumptions
        # Given list  of ints
        # List fits in memory

        # Approach
        # 1. Pop; O(N^2). For each instance of val, pop it from the list and
        # then shuffle the rest of the items towards the front.
        # 2. O(N) two pointer: slow pointer is non "val" items. Fast pointer
        # skips over val items. If fast pointer finds new non-val item it
        # writes to slow pointer.
        # In other words both pointers advance until we hit first val
        # then slow pointer stops and fast pointer finds first non-val
        # item and swaps it with val item. Then slow pointer is moved
        # until it either hits another val item or reaches the fast pointer
        # if hits another val item then it stops and fast pointer keeps going
        # if it hits fast pointer then they both are incremented until val
        # item found. If fast pointer hits end of list we are done,
        # return slow pointer index.
        # 3. binary search: binary search to find and pop instances of val
        # O(logn) to find, O(k) of num instances of val, O(n) to pop.

        # Edge cases:
        # no val in array
        # no array
        # no val


        # Let's implement approach 2
        # Given nums = [3,2,2,3], val = 3
        # [3,2,2,3]
        #    f
        #  s
        # [2,3,2,3]
        #      f
        #    s
        # [2,2,3,3]
        #        f
        #      s
        # return 2

        # Given nums = [0,1,2,2,3,0,4,2], val = 2
        # [0,1,2,2,3,0,4,2]
        #          f
        #      s

        # [0,1,2,2,3,0,4,2]
        #          f
        #      s

        # [0,1,3,2,2,0,4,2]
        #            f
        #        s

        # [0,1,3,0,2,2,4,2]
        #              f
        #          s

        # [0,1,3,0,4,2,2,2]
        #                f
        #            s
        # return 5


        # edge case check
        if len(nums) == 0 or val == None:
            return len(nums)

        slow = 0
        fast = 0

        while fast < len(nums):

            # if both equal val then move fast pointer
            if nums[fast] == val and nums[slow] == val:
                fast += 1

            # if fast is not at val but slow is, swap them then increment both
            elif nums[slow] == val:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                fast += 1
                slow += 1

            elif nums[fast] == val:
                fast += 1

            else:
                fast += 1
                slow += 1

        return slow















