# 169-Majority_Element_EASY.py

# Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

# You may assume that the array is non-empty and the majority element always exist in the array.

# Example 1:

# Input: [3,2,3]
# Output: 3
# Example 2:

# Input: [2,2,1,1,1,2,2]
# Output: 2

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        # calculate minimum, then count occurrences
        # until one element exceeds the minimum
        # Complexity = O(N) in the worst case because we
        # visit each element before finding one that meets
        # the minimum.

        minimum = len(nums) / 2

        counts = {}

        for element in nums:

            counts[element] = counts.get(element, 0) + 1

            if counts[element] > minimum:
                return element


if __name__ == '__main__':
    s = Solution()

    example_1 = {
        "example_num": 1,
        "data": [3,2,3],
        "desired_output": 3
    }

    example_2 = {
        "example_num": 2,
        "data": [2,2,1,1,1,2,2],
        "desired_output": 2
    }

    examples = [example_1, example_2]

    for example in examples:

        print(
            "Example {example_num}: {data} should output {desired_output}. Output: {output}".format(
                **example,
                output=s.majorityElement(example['data'])
            )
        )