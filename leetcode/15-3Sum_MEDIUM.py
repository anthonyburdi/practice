# 15-3Sum_MEDIUM.py

# https://leetcode.com/problems/3sum/

# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

# Note:

# The solution set must not contain duplicate triplets.

# Example:

# Given array nums = [-1, 0, 1, 2, -1, -4],

# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]

# Start: 4:04p  End: 4:45p

# Assumptions
# all are integers

# Approach
# 1. brute force: 3 pointers. Check every combination. O(n^3) time complexity
# 2. are there any duplicate subproblems? can we use dynamic programming
# somehow to help? I can't think of any...
# We may have to check all combinations
# When we find a combination that works, sort it then add as a tuple to set()
# that way we avoid duplicates
# Can we avoid checking duplicates in the first place? I think it's
# unavoidable. WE have to check all combinations and checking if the sum
# is 0 is constant time just like a lookup in the set would be.

# Maybe we can stop after finding a triplet with the first two digits and
# immediately increment since we would only find a duplicate afterward
# this is still O(N^3)

# This solution exceeds the time limit

# 3. Sort first, then iterate through only negative integers and then with both
# a pointer just after and from the end of the array try to find two other
# numbers that would make the total 0.
# O(NlogN) for the sort, then O(N^2) for the iteration (item under
# investigation, and then two pointers from front and back)
# see https://leetcode.com/problems/3sum/discuss/232712/Best-Python-Solution-(Explained)

# Edge Cases
# len(nums) <= 2: return []


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        if len(nums) <= 2:
            return []

        # Brute Force
        # answers = set()

        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         for k in range(j + 1, len(nums)):
        #             candidate = sorted([nums[i], nums[j], nums[k]])
        #             if sum(candidate) == 0:
        #                 answers.add(tuple(candidate))

        # return list(answers)

        nums.sort()
        answers = set()

        for i in range(len(nums)):
            # only check positive
            if nums[i] > 0:
                break
            left = i + 1
            right = len(nums) - 1

            while left < right:
                candidate = [nums[i], nums[left], nums[right]]

                if sum(candidate) == 0:
                    answers.add(tuple(candidate))
                    left += 1
                    right -= 1
                elif sum(candidate) > 0:
                    right -= 1
                elif sum(candidate) < 0:
                    left += 1

        return list(answers)




# Testcases
# [-1,0,1,2,-1,-4]
# [1,2]
# []
# [1]
# [1,2,3]
# [1,2,3,-3,0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# Time Limit Exceeded w/brute force:
# [13,-5,3,3,-1,13,3,1,-9,-4,9,12,6,-9,-6,-12,-8,3,12,14,4,-15,2,-11,4,-12,10,9,-6,-3,-8,14,7,3,2,-8,-7,-10,8,-8,-7,-6,-11,6,-7,-2,9,-8,8,-2,13,-10,-2,0,-14,-13,-4,11,3,-3,-7,3,-4,8,13,13,-15,-9,10,0,-2,-12,1,2,9,1,8,-4,8,-7,9,7,-2,-15,14,0,-13,-13,-12,-2,-1,-11,8,10,12,6,8,4,12,3,11,-12,-2,-3,5,-15,6,-10,-4,-1,-1,-10,13]
