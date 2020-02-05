# 56-Merge_Intervals_MEDIUM.py

# https://leetcode.com/problems/merge-intervals/

# Given a collection of intervals, merge all overlapping intervals.

# Example 1:

# Input: [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
# Example 2:

# Input: [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
# NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # Assumptions
        # intervals are ints
        # overlapping if end equals start
        # all data fits on a single machine or api is consistent for multiple
        # machines
        # Assume intervals are not sorted, even though all examples are.

        # Approach, Complexity, Tradeoffs, Potential Improvements
        # should we first sort? O(nlogn)
        # 1. Brute force for each interval iterate through the rest of the
        # intervals and if overlap modify the current and restart the iteration
        # intervals overlap if the end of the first is greater or equal to the
        # second. Then the resulting interval is the min of the first elements
        # and the max of the next elements.
        # or if one completely encloses another then the start is less and
        # the end is greater
        # This is O(N^2) time for each combination O(1) space
        # 2. Can we do it in O(N) time? Maybe.
        # I can't think of a good solution right now

        # Edge cases
        # end equals start overlapping
        # fully overlapped items
        # no items
        # single item

        # Handle small edge cases
        if len(intervals) <= 1:
            return intervals

        # Brute force
        def overlap(interval1: List, interval2: List) -> bool:
            """Return whether two intervals overlap."""
            start_1 = interval1[0]
            start_2 = interval2[0]
            end_1 = interval1[1]
            end_2 = interval2[1]

            # Surely the below can be combined, just trying to be exhaustive
            # before optimizing.

            # e.g. [1, 4] [3, 5] or [0, 1] [1, 3]
            if start_1 <= start_2 and end_1 >= start_2:
                return True

            # e.g. [1, 2] [3, 4]
            if start_1 <= start_2 and end_1 < start_2:
                return False


             # e.g. [3, 5] [1, 4]  or [1, 3] [0, 1]
            if start_2 <= start_1 and end_2 >= start_1:
                return True

            # e.g. [3, 4] [1, 2]
            if start_2 <= start_1 and end_2 < start_1:
                return False



            # e.g. [1, 9] [3, 4]
            if start_1 <= start_2 and end_1 >= end_2:
                return True

            # e.g. [4, 9] [3, 5]
            if start_1 >= start_2 and end_1 >= end_2:
                return True


            # e.g. [3, 4] [1, 9]
            if start_2 <= start_1 and end_2 >= end_1:
                return True

            # e.g. [3, 5] [4, 9]
            if start_2 >= start_1 and end_2 >= end_1:
                return True



        def _merge(interval1: List, interval2: List) -> List:
            """Merge two intervals that overlap."""
            start_1 = interval1[0]
            start_2 = interval2[0]
            end_1 = interval1[1]
            end_2 = interval2[1]

            return [min(start_1, start_2), max(end_1, end_2)]


        i = 0
        j = 1

        while i < len(intervals):
            while j < len(intervals):
                if overlap(intervals[i], intervals[j]):
                    merged = _merge(intervals[i], intervals[j])
                    intervals[i] = merged
                    intervals.pop(j)
                    # Start over
                    i = 0
                    j = 1

                else:
                    j += 1
            i += 1
            j = i + 1

        return intervals


import unittest

class TestMerge(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        i = [[1,3],[2,6],[8,10],[15,18]]
        o = [[1,6],[8,10],[15,18]]
        self.assertEqual(
            sorted(o),
            self.solution.merge(i)
        )

    def test_example_2(self):
        i = [[1,4],[4,5]]
        o = [[1,5]]
        self.assertEqual(
            sorted(o),
            self.solution.merge(i)
        )


    def test_failing_case_1(self):
        i = [[2,3],[4,5],[6,7],[8,9],[1,10]]
        o = [[1, 10]]
        self.assertEqual(
            sorted(o),
            self.solution.merge(i)
        )



    def test_failing_case_2(self):
        i = [[2,3],[2,2],[3,3],[1,3],[5,7],[2,2],[4,6]]
        o = [[1,3],[4,7]]

        self.assertEqual(
            sorted(o),
            self.solution.merge(i)
        )



if __name__ == '__main__':
    unittest.main()













