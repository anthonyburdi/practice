# 39-Combination_Sum_MEDIUM.py

# https://leetcode.com/problems/combination-sum/

# Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

# The same repeated number may be chosen from candidates unlimited number of times.

# Note:

# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# Example 1:

# Input: candidates = [2,3,6,7], target = 7,
# A solution set is:
# [
#   [7],
#   [2,2,3]
# ]
# Example 2:

# Input: candidates = [2,3,5], target = 8,
# A solution set is:
# [
#   [2,2,2,2],
#   [2,3,3],
#   [3,5]
# ]

# Start: 6:21p End:
# Start coding 6:30

# Assumptions
# Positive integers
# soultion shouldn't contain duplicate combinations

# Approach
# 1. add each digit to the current soultion_candidate until the sum is >= target
# for each choice, start over with the first candidate since there can be
# duplicates of it
# if sum is > target then disregard and stop continuing with that sol_candidate
# Time Complexity O(2^N) roughly since we check each combination but probably
# more than this because we can put the same item more than once
# Space Complexity O(2^N) since we will be storing a lot of intermediate
# solution_candidates

# Can we do better? Maybe storing intermediate results somehow?
# Yes I think we can store some
# or maybe even do a bottom up
# we can have all of the scenarios that add up to some number less than
# the target and if we get to that many left again we just look up the
# solution_candidates rather than recompute
# e.g. if target = 8 but we have two solution candidates that sum already
# to 2, then we only have to compute once the result for target = 6
# and add the result to each of the solution candidates


# Edge Cases
# target = 0
# candidates = []
from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # Edge cases
        if target == 0 or len(candidates) == 0:
            return []

        solution_candidate = []
        answer = set()

        dp = {}

        def helper(solution_candidate, candidates, target, left, answer, dp):
            if left == 0:
                answer.add(tuple(sorted(solution_candidate)))
                return

            # if not compute it
            for candidate in candidates:
                solution_candidate.append(candidate)
                curr_sum = sum(solution_candidate)
                # check if solution exists in dp, if so add it
                # if dp.get(curr_sum):
                #     for stored_candidate in dp.get(curr_sum):
                #         solution_candidate.append(stored_candidate)

                # else:
                if curr_sum <= target:
                    # add it to dp
                    # dp[curr_sum] = dp.get(curr_sum, []).append(tuple(sorted(solution_candidate)))

                    # continue finding the rest of the candidate
                    helper(solution_candidate, candidates, target, target - curr_sum, answer, dp)

                solution_candidate.pop()


            # return it
            # return solution_candidate

        helper(solution_candidate, candidates, target, target, answer, dp)

        # Convert back to list and return
        return [list(a) for a in answer]


if __name__ == '__main__':
    candidates = [2,3,6,7]
    target = 7
    s = Solution()

    print(s.combinationSum(candidates, target))

    candidates = [2,3,5]
    target = 8
    print(s.combinationSum(candidates, target))


















