# 300-Longest_Increasing_Subsequence_MEDIUM.py

# https://leetcode.com/problems/longest-increasing-subsequence/

# Given an unsorted array of integers, find the length of longest increasing subsequence.

# Example:

# Input: [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
# Note:

# There may be more than one LIS combination, it is only necessary for you to return the length.
# Your algorithm should run in O(n2) complexity.
# Follow up: Could you improve it to O(n log n) time complexity?

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        # Assumptions
        # nums can include negative numbers and 0
        # nums fits on a single machine
        # increasing means that equal items don't count (will need to check)
        # looks like the case based on problem output.

        # Approach, Complexity, Tradeoffs, Potential Improvements

        # 1. Generate all subsequences and check whether they are max
        # O(2^n) time complexity so not the optimal

        # 2. for each item iterate throught the rest picking out any
        # items that are bigger than the last
        # when we reach the end of the array then check the length against
        # any previous maximum
        # Time complexity O(N^2) since we traverse O(n*(n-1)) for each n
        # space complexity O(1)
        # Can we do better?

        # 3. What if we iterate through and change each item to a tuple
        # with the (original number, original index) which is O(N)
        # then sort it in O(nlogn)
        # then we just look for the longest increasing indices, and we don't
        # have to check for all possibilities bc since the array is sorted
        # based on the original values we just want to make sure that those
        # values occur after each other. This last step is O(N)
        # so this whole algorithm is O(NlogN) time complexity. We do have
        # an additional sorted array of tuples so the space complexity is
        # now higher at O(N) but that may be an OK tradeoff.

        # Edge cases
        # negative numbers (should be fine with our algorithm)
        # 0 (should be fine with our algorithm)
        # empty nums - return 0
        # single item - return 1
        # two items (should be fine with our algorithm)

        # Manual test
        # [10,9,2,5,3,7,101,18] should yield 4: [2,3,7,101]
        # Sorted w tuples of (original number, original index):
        # [(2, 2),(3, 4),(5, 3),(7, 5),(9, 1),(10, 0),(18, 7),(101, 6)]
        # longest index increasing is 2,3,5,6
        # hmm this doesn't appear to help our cause. We still have to drop
        # non obvious items... this is a pretty good test case.

        # Let's code approach 2 and think more

        # Wrong answer with current approach 2 :(
        # [10,9,2,5,3,4]
        # Output = 2
        # Expected = 3
        # duh, this will never include the 2 with the 3, 4 since the 5 meets
        # its criteria.

        # See solutions - memoized dynamic programming solution is required
        # or using binary search.

        # Original try
        # #  edge cases:
        # if len(nums) <= 1:
        #     return len(nums)

        # i = 0
        # current_max = 0

        # while i < len(nums):
        #     j = i + 1
        #     current_list = [nums[i]]

        #     while j < len(nums):
        #         if nums[j] > current_list[-1]:
        #             current_list.append(nums[j])

        #         j += 1

        #     if len(current_list) > current_max:
        #         current_max = len(current_list)

        #     i += 1

        # return current_max

        # Fixed

        #  edge cases:
        if len(nums) == 0:
            return len(nums)

        i = 1
        max_to_i = [1] * len(nums)

        overall_max = 1

        while i < len(nums):
            current_max = 0

            j = 0

            while j < i:
                if nums[i] > nums[j]:
                    current_max = max(current_max, max_to_i[j])
                j += 1

            max_to_i[i] = current_max + 1
            overall_max = max(overall_max, max_to_i[i])

            i += 1

        return overall_max
