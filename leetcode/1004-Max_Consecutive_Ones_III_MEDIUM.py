# 1004-Max_Consecutive_Ones_III_MEDIUM.py

# https://leetcode.com/problems/max-consecutive-ones-iii/

# Given an array A of 0s and 1s, we may change up to K values from 0 to 1.

# Return the length of the longest (contiguous) subarray that contains only 1s.



# Example 1:

# Input: A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
# Output: 6
# Explanation:
# [1,1,1,0,0,1,1,1,1,1,1]
# Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.
# Example 2:

# Input: A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
# Output: 10
# Explanation:
# [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
# Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.


# Note:

# 1 <= A.length <= 20000
# 0 <= K <= A.length
# A[i] is 0 or 1

from typing import List

class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        # Assumptions
        # See question "Note"

        # Approach
        # Iterate through counting 0's for current subarray
        # Store pointer for beginning of subarray and end, num of 1's
        # (incl switched ones)
        # When subarray has exceeded the number of 0's allowed (k) then move
        # the pointers forward. If the added right digit is a 1, compare the
        # new length of the subarray to the max found so far, move right pointer.
        # If it is a 0, check the number of 0's found wrt k.
        # if num_zeroes == k then note the length and check against max
        # found so far. Then move both pointers.
        # if the added digit is a 1, then only move the right pointer
        # If the left digit is not a 0, keep moving it forward until num_zeroes
        # is = k. If the next digit is a 0 and num_zeroes = k, move it again

        # Complexity
        # Time O(N) since we visit each digit once
        # Space O(1) since we only store a few pointers & counts

        # Potential Improvements
        # I can't think of any...

        # Edge Cases
        # empty list
        # K = 0
        # sequence at beginning or end
        # very short sequence

        left = 0
        right = 0
        max_len = 0
        num_zeroes = 0

        while right < len(A):
            if A[right] == 0:
                num_zeroes += 1

                # Keep moving left until we remove a 0 and num_zeroes < K

                while num_zeroes > K:
                    if A[left] == 0:
                        num_zeroes -= 1
                    left += 1

            curr_len = right - left + 1
            if curr_len > max_len:
                max_len = curr_len

            right += 1

        return max_len



        # Test cases:
        # Example 1:

        #            [0,1,2,3,4,5,6,7,8,9,10]
        # Input: A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
        # Output: 6
        # Explanation:
        # [1,1,1,0,0,1,1,1,1,1,1]
        # Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.

        # {left: 0, right: 0, A[right]: 1, num_zeroes: 0, A[left]: 1, num_zeroes: 0, left: 0, curr_len: 1, max_len: 1, right: 1}
        # {left: 0, right: 1, A[right]: 1, num_zeroes: 0, A[left]: 1, num_zeroes: 0, left: 0, curr_len: 2, max_len: 2, right: 2}
        # {left: 0, right: 2, A[right]: 1, num_zeroes: 0, A[left]: 1, num_zeroes: 0, left: 0, curr_len: 3, max_len: 3, right: 3}
        # {left: 0, right: 3, A[right]: 0, num_zeroes: 1, A[left]: 1, num_zeroes: 1, left: 0, curr_len: 4, max_len: 4, right: 4}
        # {left: 0, right: 4, A[right]: 0, num_zeroes: 2, A[left]: 1, num_zeroes: 2, left: 0, curr_len: 5, max_len: 5, right: 5}

        # {left: 0, right: 5, A[right]: 0, num_zeroes: 3, A[left]: 1, num_zeroes: 3, left: 1, ---- curr_len: 5, max_len: 5, right: 5}
        # {left: 1, right: 5, A[right]: 0, num_zeroes: 3, A[left]: 1, num_zeroes: 3, left: 2, ---- curr_len: 5, max_len: 5, right: 5}
        # {left: 2, right: 5, A[right]: 0, num_zeroes: 3, A[left]: 1, num_zeroes: 3, left: 3, ---- curr_len: 5, max_len: 5, right: 5}
        # {left: 3, right: 5, A[right]: 0, num_zeroes: 3, A[left]: 0, num_zeroes: 2, left: 4, ---- curr_len: 5, max_len: 5, right: 5}

        # {left: 4, right: 5, A[right]: 0, num_zeroes: 2, A[left]: 0, num_zeroes: 2, left: 4, curr_len: 2, max_len: 5, right: 6}
        # {left: 4, right: 6, A[right]: 1, num_zeroes: 2, A[left]: 0, num_zeroes: 2, left: 4, curr_len: 3, max_len: 5, right: 7}
        # {left: 4, right: 7, A[right]: 1, num_zeroes: 2, A[left]: 0, num_zeroes: 2, left: 4, curr_len: 4, max_len: 5, right: 8}
        # {left: 4, right: 8, A[right]: 1, num_zeroes: 2, A[left]: 0, num_zeroes: 2, left: 4, curr_len: 5, max_len: 5, right: 9}
        # {left: 4, right: 9, A[right]: 1, num_zeroes: 2, A[left]: 0, num_zeroes: 2, left: 4, curr_len: 6, max_len: 6, right: 10}
        # {left: 4, right: 10,A[right]: 0, num_zeroes: 3, A[left]: 0, num_zeroes: 2, left: 5, curr_len: 6, max_len: 6, right: 11}
        # end loop 11 > len(A)
        # return 6


import unittest

class TestLongestOnes(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):

        # Input:
        A = [1,1,1,0,0,0,1,1,1,1,0]
        K = 2
        # Output:
        output = 6

        self.assertEqual(self.solution.longestOnes(A, K), output)


    def test_example_2(self):

        # Input:
        A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
        K = 3
        # Output:
        output = 10

        self.assertEqual(self.solution.longestOnes(A, K), output)


    # Edge Cases
    # empty list
    # K = 0
    # sequence at beginning or end
    # very short sequence

    def test_empty_list(self):

        # Input:
        A = []
        K = 0
        # Output:
        output = 0

        self.assertEqual(self.solution.longestOnes(A, K), output)


    def test_k_is_zero(self):

        # Input:
        A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
        K = 0
        # Output:
        output = 4

        self.assertEqual(self.solution.longestOnes(A, K), output)

        # Input:
        A = [1,1,1,0,0,0,1,1,1,1,0]
        K = 0
        # Output:
        output = 4

        self.assertEqual(self.solution.longestOnes(A, K), output)


    def test_sequence_at_beginning_or_end(self):

        # Input:
        A = [0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,0]
        K = 2
        # Output:
        output = 12

        self.assertEqual(self.solution.longestOnes(A, K), output)

        # Input:
        A = [1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,0]
        K = 2
        # Output:
        output = 10

        self.assertEqual(self.solution.longestOnes(A, K), output)


        # Input:
        A = [0,1,1,1,1,0,0,0,1,1,1,1,0,1,1,1,1,0]
        K = 2
        # Output:
        output = 10

        self.assertEqual(self.solution.longestOnes(A, K), output)

        # Input:
        A = [1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        K = 2
        # Output:
        output = 23

        self.assertEqual(self.solution.longestOnes(A, K), output)

    def test_k_is_length_of_a(self):

        # Input:
        A = [0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,0]
        K = 19
        # Output:
        output = 19

        self.assertEqual(self.solution.longestOnes(A, K), output)


        # Input:
        A = [1,1,1,1,1,1,1,1]
        K = 8
        # Output:
        output = 8

        self.assertEqual(self.solution.longestOnes(A, K), output)

        # Input:
        A = [0,0,0,0,0,0,0,0]
        K = 8
        # Output:
        output = 8

        self.assertEqual(self.solution.longestOnes(A, K), output)

    def test_short_sequences(self):

        # Input:
        A = [1]
        K = 1
        # Output:
        output = 1

        self.assertEqual(self.solution.longestOnes(A, K), output)

        # Input:
        A = [0]
        K = 1
        # Output:
        output = 1

        self.assertEqual(self.solution.longestOnes(A, K), output)

        # Input:
        A = [0]
        K = 0
        # Output:
        output = 0

        self.assertEqual(self.solution.longestOnes(A, K), output)


if __name__ == '__main__':
    unittest.main()

