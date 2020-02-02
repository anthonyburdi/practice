# 14-Longest_Common_Prefix_EASY.py

# https://leetcode.com/problems/longest-common-prefix/

# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Example 1:

# Input: ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# Note:

# All given inputs are in lowercase letters a-z.

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        prefix = []

        if strs == []:
            return ''

        i = 0
        while True:
            curr_char = None
            for s in strs:
                if i >= len(s):
                    return "".join(prefix)
                else:
                    if curr_char == None:
                        curr_char = s[i]
                    elif s[i] != curr_char:
                        return "".join(prefix)

            i += 1
            prefix.append(curr_char)


