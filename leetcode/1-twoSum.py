# 1-twoSum.py
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # convert list to difference from target
        # e.g. for example [2, 7, 11, 15] it would be [7, 2, -2, -6]
        # convert this to a hashmap with indices as values, e.g.
        # {7: 0, 2: 1, -2: 2, -6, 3}
        # then loop through the list of numbers
        # for each item check if that item exists in the hashmap keys
        # if it does then use the index of the current item and the value from the
        # hashmap for the indices

        differences = [target - num for num in nums]
        differences_hashmap = {}
        for idx, item in enumerate(differences):
            differences_hashmap[item] = idx

        print(differences)
        print(differences_hashmap)

        for jdx, num in enumerate(nums):

            print(jdx, num)
            if num in differences_hashmap:
                # we don't want repeated values, so check for them and skip
                if jdx == differences_hashmap[num]:
                    continue
                # we could return sorted([jdx, differences_hashmap[num]])
                # so that the lowest index is first
                # this should not matter though since we are starting from
                # the first values and should catch the earliest
                return [jdx, differences_hashmap[num]]

        # if we find nothing return an empty list
        return []


if __name__ == '__main__':
    solution = Solution()

    print("Should be [0, 1]. My answer:", solution.twoSum([2,7,11,15], 9))

    print("Should be [1, 2]. My answer:", solution.twoSum([3, 2, 4], 6))