# 278-First_Bad_Version_EASY.py

# https://leetcode.com/problems/first-bad-version/

# You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

# Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

# You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

# Example:

# Given n = 5, and version = 4 is the first bad version.

# call isBadVersion(3) -> false
# call isBadVersion(5) -> true
# call isBadVersion(4) -> true

# Then 4 is the first bad version.

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """

        # implement using binary search
        # start with full search space (1, n)
        # check midpoint
        # if midpoint is bad, then set mid as latest bad
        # then move right to mid and check the next section
        # if mid is not bad then move left to mid
        # finally if our pointers overlap return the first_bad

        left = 1
        right = n
        first_bad = n

        while left <= right:
            curr_version = left + (right - left) // 2
            curr_version_is_bad = isBadVersion(curr_version)
            if curr_version_is_bad:
                right = curr_version - 1
                if curr_version < first_bad:
                    first_bad = curr_version
            if not curr_version_is_bad:
                left = curr_version + 1

        return first_bad


        # Example
#         n = 1000
#         v = 100
#         left = 1; right = 1000
#         curr_version = 1 + (1000 - 1) // 2 = 500
#         curr_version_is_bad == True
#         right = 500 - 1 = 499; left = 1
#         first_bad = 500

#         curr_version = 1 + (499 - 1) // 2 = 250
#         curr_version_is_bad == True
#         right = 250 - 1 = 249; left = 1
#         first_bad = 250

#         curr_version = 1 + (249 - 1) // 2 = 125
#         curr_version_is_bad == True
#         right = 125 - 1 = 124; left = 1
#         first_bad = 125

#         curr_version = 1 + (124 - 1) // 2 = 62
#         curr_version_is_bad == False
#         right = 124; left = 63

#         curr_version = 63 + (124 - 63) // 2 = 93
#         curr_version_is_bad == False
#         right = 124; left = 94

#         curr_version = 94 + (124 - 94) // 2 = 109
#         curr_version_is_bad == True
#         right = 108; left = 94
#         first_bad = 109

#         curr_version = 94 + (108 - 94) // 2 = 101
#         curr_version_is_bad == True
#         right = 100; left = 94
#         first_bad = 101

#         curr_version = 94 + (100 - 94) // 2 = 97
#         curr_version_is_bad == False
#         right = 100; left = 97 + 1 = 98

#         curr_version = left + (right - left) // 2
#         curr_version = 98 + (100 - 98) // 2 = 99
#         curr_version_is_bad == False
#         right = 100; left = 99 + 1 = 100
#         first_bad = 101
#         BREAK
#         return first_bad == 101 WRONG

        # If we don't break but change to while left <= right

#         curr_version = left + (right - left) // 2
#         curr_version = 100 + (100 - 100) // 2 = 100
#         curr_version_is_bad == True
#         right = 100 - 1 = 99; left = 100
#         first_bad = 100

        # alternative:
        # if we change to check  if left == right then check
        # left ==  right == mid if bad and return it if lower
        # than first_bad?

        # curr_version = left + (right - left) // 2
        # curr_version = left + (right - left) // 2 = ?
        # curr_version_is_bad == ?
        # right = ?; left = ?
        # first_bad = ?