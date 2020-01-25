# 347-Top_K_Frequent_Elements_MEDIUM.py

# https://leetcode.com/problems/top-k-frequent-elements/

# Given a non-empty array of integers, return the k most frequent elements.

# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]
# Note:

# You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
# Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Assumptions
        # See problem statement (1 <= k <= num unique elements, O(n log n) max,
        # non-empty array of integers)

        # Approach
        # use a loop and hashmap to count each element
        # keep the top k items in an ordered array as a item:value pair
        # actually better to keep separate list for item and value
        # in same order (e.g. count of item[0] is value[0])
        # Also keep set of items for updates so we can quickly find if it
        # exists
        # if the next item inserted is bigger than the min item in the ordered
        # array, then replace it
        # return the items from the ordered array

        # Complexity
        # Time: O(N) to count each element, constant time for all other ops
        # (except for the return which is O(k) - unless we use 2 lists)
        # Space: O(k) for the counts and O(n) for the hashmap (of n unique
        # elements) and the set() so O(n) overall.

        # Potential improvements
        # I can't think of any. Maybe if there are less additional items
        # to check in the list and no way for any values to change position
        # we can stop. Requires more space for all items to be in the list

        # OK potential improvement: store top items as dict. Store min
        # value. If higher than min value then drop min value and instead
        # put current value.
        # I don't think this can work bc how do we drop the min value
        # We have to find the min value again and then drop it, not the
        # other values in the top lists.

        # We can use a heap or collections.Counter instead to keep track
        # of the most frequent elements.

        # Edge cases
        # k = 1 and single element
        # negative integers
        # zero
        # k = num of unique elements

        # IMPLEMENTATION -------------------------------------------------------

        # Initialize
        counts = {}
        top_items = []
        top_values = []
        top_items_set = set(top_items)

        # Count each element
        for element in nums:

            # update count
            counts[element] = counts.get(element, 0) + 1

        #     if element in top_items_set:
        #         i = top_items.index(element)
        #         top_values[i] += counts[element]

        #     # insert into top lists if not full
        #     elif len(top_items) < k:
        #         top_items.append(element)
        #         top_values.append(counts[element])
        #         top_items_set = set(top_items)

        #     # insert into top lists if bigger than smallest item
        #     elif (
        #         (element not in top_items) and
        #         (counts[element] > min(top_values))
        #     ):
        #         min_index = top_values.index(min(top_values))
        #         top_items.pop(min_index)
        #         top_values.pop(min_index)
        #         top_items.append(element)
        #         top_values.append(counts[element])
        #         top_items_set = set(top_items)

        # return top_items

        top_k_items = sorted(list(counts.values()))[-k:]
        counts_to_items = [(k, v) for k, v in counts.items()]
        from operator import itemgetter
        counts_to_items.sort(key=itemgetter(1), reverse=True)
        return [i[0] for i in counts_to_items[0:k]]




# Test Cases

# Input
# [4,1,-1,2,-1,2,3]
# 2
# Output
# [4,2]
# Expected
# [-1,2]

import unittest

class TestTopKFrequent(unittest.TestCase):

    def setUp(self):

        self.solution = Solution()

    def test_case_with_issue(self):

        nums = [4,1,-1,2,-1,2,3]
        k = 2
        output = [-1, 2]

        self.assertEqual(
            sorted(self.solution.topKFrequent(nums, k)),
            sorted(output)
        )


    def test_case_with_issue2(self):

        nums = [5,2,5,3,5,3,1,1,3]
        k = 2
        output = [3,5]

        self.assertEqual(
            sorted(self.solution.topKFrequent(nums, k)),
            sorted(output)
        )

    def test_case_with_issue3(self):
        nums = [-5,-9,67,-10,4,-57,47,13,-67,-26,-57,63,38,-68,62,-45,-37,95,49,-91,-53,-42,-33,80,78,-30,-36,22,9,-86,79,-1,44,-92,30,-68,-94,58,-51,-26,-38,5,-74,25,71,-93,52,-12,-86,7,-86,53,78,-31,-5,-87,88,-98,-39,9,99,23,96,-90,51,-64,35,-73,9,60,-78,70,99,14,70,71,-78,50,7,46,-89,57,-1,87,-87,-95,48,49,79,-54,31,28,-27,75,31,-76,-12,35,40,-90,-60,-60,-7,67,73,-34,-42,-35,61,51,18,95,16,78,-81,-91,-30,92,57,-79,5,41,29,72,-62,-47,80,29,1,-21,-36,5,82,4,-12,-52,-56,-47,-68,95,85,-87,-7,-12,98,75,-64,-93,11,73,-81,-9,-12,-9,51,17,-94,33,-9,57,-35,10,-17,87,-18,-55,-52,30,-62,73,35,-74,-47,-63,77,-72,-55,5,73,21,14,7,-65,-51,-55,-49,98,-20,-22,-68,34,-20,92,55,47,-20,6,-54,-12,3,75,69,60,15,88,64,2,-27,-50,55,73,46,-15,-64,93,-47,-75,-55,-75,21,-57,91,-12,-99,-68,-56,-14,-4,-77,-94,55,93,-31,68,-12,-23,59,-56,-86,43,83,-93,-78,-11,-7,96,-3,-87,-37,19,-78,67,-29,77,-28,91,-73,-68,-22,18,-7,3,15,77,99,31,-48,-86,-45,-82,52,-39,8,-88,-83,-58,-77,5,87,-61,50,32,-66,-36,60,-53,52,70,-36,-1,83,-56,33,98,-80,28,1,-21,-50,-60,44,99,18,83,-29,83,-36,-55,-6,96,-60,61,75,6,-57,2,82,62,-27,36,60,72,92,61,-65,79,-57,-34,-23,-28,-55,53,36,-80,5,-76,64,-81,-32,-43,-1,50,-16,-72,-74,22,88,28,-79,-99,85,-13,-34,-76,85,6,21,-99,10,-46,79,11,-70,17,47,-22,-62,0,6,75,-19,57,-25,-52,-83,90,21,95,52,68,47,-12,76,-9,-65,86,90,16,74,64,26,84,64,-42,97,-72,53,-76,11,89,-62,67,100,15,53,68,-16,24,11,-77,20,59,-95,-50,-20,27,45,94,13,-93,86,49,12,19,17,-33,-52,-28,71,79,-19,-73,40,-99,83,77,19,-20,98,86,-5,-5,73,18,100,73,-45,33,3,89,32,-53,73,16,-3,-26,-80,49,-78,67,31,1,-85,-44,-91,-68,75,-74,95,23,89,99,-84,54,-93,68,0,-41,66,-15,-27,-23,-9,-68,37,45,-69,57,80,10,-64,35,26,55,-67,31,-76,36,-99,21]
        k = 7
        output = [-12,-68,73,-55,-9,75,5]

        self.assertEqual(
            sorted(self.solution.topKFrequent(nums, k)),
            sorted(output)
        )



if __name__ == "__main__":
    unittest.main()














