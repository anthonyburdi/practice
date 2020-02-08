# 88-Merge_Sorted_Array_EASY.py

# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

# Note:

# The number of elements initialized in nums1 and nums2 are m and n respectively.
# You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
# Example:

# Input:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3

# Output: [1,2,2,3,5,6]

# Example 2:
# Input:
# [0]
# 0
# [1]
# 1
# Output: [1]

# Example 3:
# Input:
# [2,0]
# 1
# [1]
# 1

from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # if too small just return
        if len(nums1) == 0:
            return

        # # let's first copy nums1 digits to the rear so we have space
        # # to start pulling in nums2

        # for i in range(m):
        #     nums1[i + m] = nums1[i]

        # # then we can compare the digits in nums1 with nums2 and add the smaller
        # # one to the beginning of nums1

        # # we need three pointers one each for nums1 and nums2 and one for the insertion
        # insert_idx = 0
        # nums1_idx = m # start at the second half of nums1
        # nums2_idx = 0

        # while insert_idx < (m + n):

        #     # find the next item to insert
        #     # make sure we don't go off the end of either array
        #     if (nums1_idx < (2 * m)) and (nums1[nums1_idx] <= nums2[nums2_idx]):
        #         nums1[insert_idx] = nums1[nums1_idx]
        #         nums1_idx += 1
        #     elif (nums2_idx < n):
        #         nums1[insert_idx] = nums2[nums2_idx]
        #         nums2_idx += 1
        #     else:
        #         nums1[insert_idx] = nums1[nums1_idx]
        #         nums1_idx += 1
        #     insert_idx += 1

        # # Time Complexity: O(m + (m + n)) since we loop through each array a single time
        # # and once to move the nums1 data to the end of the list
        # # we can say this is O(N) time

        # # Space complexity: O(N) (really O(m + (m + n))) since we don't create more arrays

        # Very similar approach but start with the end of nums1 with the largest
        # item and work forwards so we only need one pass

        insert_idx = len(nums1) - 1
        nums1_idx = m - 1
        nums2_idx = n - 1

        # if we exhaust inserts or we exhaust nums2 then we are merged
        while insert_idx >= 0 and nums2_idx >= 0:

            # pick the larger of the two values to insert at insert_idx
            # or if equal put in the value from nums1 (arbitrarily)
            # also if we ran out of nums1 then just insert all of nums2
            if (nums1_idx < 0) or (nums2[nums2_idx] > nums1[nums1_idx]):
                nums1[insert_idx] = nums2[nums2_idx]
                # then move the pointer for the inserted value
                nums2_idx -= 1

            else:
                nums1[insert_idx] = nums1[nums1_idx]
                # then move the pointer for the inserted value
                nums1_idx -= 1

            # finally move the insert_idx
            insert_idx -= 1


        # manual test
        # nums1 = [2,0] m = 1
        # nums2 = [1] n = 1
        # o = [1, 2]

        # pointers = insert_idx, nums1_idx, nums2_idx

        # pointers = 1, 0, 0
        # n1 = 2 n2 = 1 so nums1[1] = n1 n1i = -1
        # [2,2] , [1]
        # pointers = 0, -1, 0
        # n1i < 0 so nums1[0] = n2 n2i = -1
        # [1,2] , [1]
        # while loop exited


        # manual test
        # nums1 = [1,2,3,0,0,0], m = 3
        # nums2 = [2,5,6],       n = 3
        # Output: [1,2,2,3,5,6]

        # pointers = insert_idx, nums1_idx, nums2_idx

        # pointers = 5, 2, 2
        # n1 = 3 n2 = 6 so nums1[5] = n2 n2i = 1
        # [1,2,3,0,0,6] , [2,5,6]

        # pointers = 4, 2, 1
        # n1 = 3  n2 = 5 so nums1[4] = n2 n2i = 0
        # [1,2,3,0,5,6] , [2,5,6]

        # pointers = 3, 2, 0
        # n1 = 3 n2 = 2 so nums1[3] = n1 n1i = 1
        # [1,2,3,3,5,6] , [2,5,6]

        # pointers = 2, 1, 0
        # n1 = 2 n2 = 2 so nums1[2] = n1 n1i = 0
        # [1,2,2,3,5,6] , [2,5,6]

        # pointers = 1, 0, 0
        # n1 = 1 n2 = 2 so nums1[1] = n2 n2i = -1
        # [1,2,2,3,5,6] , [2,5,6]
        # while loop exited


import unittest

class TestMerge(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()


    def test_example_1(self):
        # Testing
        nums1 = [1,2,3,0,0,0]
        m = 3
        nums2 = [2,5,6]
        n = 3

        o = [1,2,2,3,5,6]

        self.solution.merge(nums1, m, nums2, n)

        self.assertEqual(o, nums1)

    def test_example_2(self):

        nums1 = [2,0]
        m = 1
        nums2 = [1]
        n = 1

        o = [1, 2]

        self.solution.merge(nums1, m, nums2, n)

        self.assertEqual(o, nums1)

    def test_edge_cases_1(self):

        nums1 = []
        m = 0
        nums2 = []
        n = 0
        o = []

        self.solution.merge(nums1, m, nums2, n)

        self.assertEqual(o, nums1)


    def test_edge_cases_2(self):
        nums1 = [0]
        m = 0
        nums2 = [1]
        n = 1
        o = [1]

        self.solution.merge(nums1, m, nums2, n)

        self.assertEqual(o, nums1)


    def test_edge_cases_3(self):
        nums1 = [0,0,0,0,0]
        m = 0
        nums2 = [1,2,3,4,5]
        n = 5
        o = [1,2,3,4,5]

        self.solution.merge(nums1, m, nums2, n)

        self.assertEqual(o, nums1)



if __name__ == '__main__':
    unittest.main()





