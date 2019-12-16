# 49-groupAnagrams.py

# 49. Group Anagrams
# Medium

# 2303

# 138

# Favorite

# Share
# Given an array of strings, group anagrams together.

# Example:

# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
# Note:

# All inputs will be in lowercase.
# The order of your output does not matter.

from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # loop through input, sorting to create the key of a hashmap
        # then appending the value (unsorted)
        # return the list of values of the hashmap

        anagrams = {}

        for s in strs:
            s_sorted = "".join(sorted(s))
            if anagrams.get(s_sorted):
                anagrams[s_sorted].append(s)
            else:
                anagrams[s_sorted] = [s]

        return list(anagrams.values())

if __name__ == '__main__':
    solution = Solution()

    inp = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(solution.groupAnagrams(inp))