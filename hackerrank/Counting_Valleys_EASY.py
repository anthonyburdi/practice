# Counting_Valleys_EASY.py

# https://www.hackerrank.com/challenges/counting-valleys/problem

# Gary is an avid hiker. He tracks his hikes meticulously, paying close attention to small details like topography. During his last hike he took exactly  steps. For every step he took, he noted if it was an uphill, , or a downhill,  step. Gary's hikes start and end at sea level and each step up or down represents a  unit change in altitude. We define the following terms:

# A mountain is a sequence of consecutive steps above sea level, starting with a step up from sea level and ending with a step down to sea level.
# A valley is a sequence of consecutive steps below sea level, starting with a step down from sea level and ending with a step up to sea level.
# Given Gary's sequence of up and down steps during his last hike, find and print the number of valleys he walked through.

# For example, if Gary's path is , he first enters a valley  units deep. Then he climbs out an up onto a mountain  units high. Finally, he returns to sea level and ends his hike.

# Function Description

# Complete the countingValleys function in the editor below. It must return an integer that denotes the number of valleys Gary traversed.

# countingValleys has the following parameter(s):

# n: the number of steps Gary takes
# s: a string describing his path
# Input Format

# The first line contains an integer , the number of steps in Gary's hike.
# The second line contains a single string , of  characters that describe his path.

# Constraints

# Output Format

# Print a single integer that denotes the number of valleys Gary walked through during his hike.

# Sample Input

# 8
# UDDDUDUU
# Sample Output

# 1
# Explanation

# If we represent _ as sea level, a step up as /, and a step down as \, Gary's hike can be drawn as:

# _/\      _
#    \    /
#     \/\/
# He enters and leaves one valley.


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    # Assumptions
    # Valley is defined as descending from sea level then back up to
    # sea level.
    # Hikes start at sea level and end at sea level.

    # Approach
    # iterate through steps and keep track of count of U and D
    # if we start with a D from sea level, keep iterating until we return
    # to sea level then add 1 to count of valleys. if we start with U from
    # sea level keep iterating until we return to sea level then reset counters
    # if num_up == num_down we are back at sea level.
    # actually just keep track of the height. Subtract from height when desc
    # and add when asc.
    # if height goes negative from 0 then add 1 valley

    # Complexity
    # Time: O(N) since we loop through each step
    # Space: O(1) since we just keep track of a few counters
    # Potential Improvements / Tradeoffs
    # I can't think of any.

    # Edge Cases
    # two steps /\ or \/

    height = 0
    valleys = 0

    for step in s:
        if height == 0 and step == "D":
            valleys += 1

        if step == "D":
            height -= 1
        elif step  == "U":
            height += 1

    return valleys

import unittest

class TestCountingValleys(unittest.TestCase):

    def test_example_1(self):
        steps = ["D", "D", "U", "U", "U", "U", "D", "D"]
        n = 7
        valleys = 1
        self.assertEqual(countingValleys(n, steps), valleys)

    def test_example_2(self):
        steps = ["U", "D", "D", "D", "U", "D", "U", "U"]
        n = 8
        valleys = 1
        self.assertEqual(countingValleys(n, steps), valleys)


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # n = int(input())

    # s = input()

    # result = countingValleys(n, s)

    # fptr.write(str(result) + '\n')

    # fptr.close()

    unittest.main()
