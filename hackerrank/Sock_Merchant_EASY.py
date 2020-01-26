# Sock_Merchant_EASY.py

# https://www.hackerrank.com/challenges/sock-merchant/problem

# https://www.hackerrank.com/challenges/sock-merchant/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

# John works at a clothing store. He has a large pile of socks that he must pair by color for sale. Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.

# For example, there are  socks with colors . There is one pair of color  and one of color . There are three odd socks left, one of each color. The number of pairs is .

# Function Description

# Complete the sockMerchant function in the editor below. It must return an integer representing the number of matching pairs of socks that are available.

# sockMerchant has the following parameter(s):

# n: the number of socks in the pile
# ar: the colors of each sock
# Input Format

# The first line contains an integer , the number of socks represented in .
# The second line contains  space-separated integers describing the colors  of the socks in the pile.

# Constraints

#  where
# Output Format

# Return the total number of matching pairs of socks that John can sell.

# Sample Input

# 9
# 10 20 20 10 10 30 50 10 20
# Sample Output

# 3
# Explanation

# sock.png

# John can match three pairs of socks.


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):

    # Assumptions
    # n and ar are integers
    # both fit on a single machine

    # Approach
    # Since we only want num of pairs (not configuration) we can use a set
    # instead of a hashmap to count. We iterate through ar and check for
    # existence in the set. If it doesn't exist, add it. If it does exist
    # then remove it and add 1 to the counter of num pairs.

    # Complexity
    # Time O(N) since we check each item. Since set lookup, insertion & removal
    # is O(1) overall we are still  O(N)
    # Space: O(N) since we store the items in a set. Less than n items but
    # still of order N. in the worst case where all socks are different we
    # will eventually store N items in the set.

    # Potential Improvements
    # we could do a two pointer approach in place and reduce the space
    # complexity to O(1) at the expense of time complexity. E.g. for each
    # sock, search the rest of the array for it's pair and if found pop both
    # out of the array and add 1 pair to counter. If no pair found pop the
    # unpaired sock. Continue until the array is empty.

    # Edge Cases
    # single item
    # no items (not given, see problem statement)

    # IMPLEMENTATION -----------------------------------------------------------
    unpaired_socks = set()
    num_pairs = 0
    for sock in ar:
        if sock not in unpaired_socks:
            unpaired_socks.add(sock)
        else:
            num_pairs += 1
            unpaired_socks.remove(sock)

    return num_pairs


import unittest

class TestSockMerchant(unittest.TestCase):

    def test_example_1(self):
        n = 9
        socks = [10, 20, 20, 10, 10, 30, 50, 10, 20]
        output = 3
        self.assertEqual(sockMerchant(n, socks), output)

    def test_example_2(self):
        n = 7
        socks = [1,2,1,2,1,3,2]
        output = 2
        self.assertEqual(sockMerchant(n, socks), output)

    def test_edge_cases(self):
        n = 1
        socks = [1]
        output = 0
        self.assertEqual(sockMerchant(n, socks), output)


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # n = int(input())

    # ar = list(map(int, input().rstrip().split()))

    # result = sockMerchant(n, ar)

    # fptr.write(str(result) + '\n')

    # fptr.close()
    unittest.main()
