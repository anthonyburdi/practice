# Frequency_Queries_MEDIUM.py

# https://www.hackerrank.com/challenges/frequency-queries/problem

# You are given  queries. Each query is of the form two integers described below:
# -  : Insert x in your data structure.
# -  : Delete one occurence of y from your data structure, if present.
# -  : Check if any integer is present whose frequency is exactly . If yes, print 1 else 0.

# The queries are given in the form of a 2-D array  of size  where  contains the operation, and  contains the data element. For example, you are given array . The results of each operation are:

# Operation   Array   Output
# (1,1)       [1]
# (2,2)       [1]
# (3,2)                   0
# (1,1)       [1,1]
# (1,1)       [1,1,1]
# (2,1)       [1,1]
# (3,2)                   1
# Return an array with the output: .

# Function Description

# Complete the freqQuery function in the editor below. It must return an array of integers where each element is a  if there is at least one element value with the queried number of occurrences in the current array, or 0 if there is not.

# freqQuery has the following parameter(s):

# queries: a 2-d array of integers
# Input Format

# The first line contains of an integer , the number of queries.
# Each of the next  lines contains two integers denoting the 2-d array .

# Constraints

# All
# Output Format

# Return an integer array consisting of all the outputs of queries of type .

# Sample Input 0

# 8
# 1 5
# 1 6
# 3 2
# 1 10
# 1 10
# 1 6
# 2 5
# 3 2
# Sample Output 0

# 0
# 1
# Explanation 0

# For the first query of type , there is no integer whose frequency is  (). So answer is .
# For the second query of type , there are two integers in  whose frequency is  (integers =  and ). So, the answer is .

# Sample Input 1

# 4
# 3 4
# 2 1003
# 1 16
# 3 1
# Sample Output 1

# 0
# 1
# Explanation 1

# For the first query of type , there is no integer of frequency . The answer is .
# For the second query of type , there is one integer,  of frequency  so the answer is .

# Sample Input 2

# 10
# 1 3
# 2 3
# 3 2
# 1 4
# 1 5
# 1 5
# 1 4
# 3 2
# 2 4
# 3 2
# Sample Output 2

# 0
# 1
# 1
# Explanation 2

# When the first output query is run, the array is empty. We insert two 's and two 's before the second output query,  so there are two instances of elements occurring twice. We delete a  and run the same query. Now only the instances of  satisfy the query.


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the freqQuery function below.
def freqQuery(queries):

    # Assumptions
    # all items are integers

    # Approach
    # Create frequency hashmap with queries {num: num_occurrences}
    # Create hashmap of num digits with frequency {freq: num_items_w_freq}
    # quickly look at hashmap of num_digits_w_frequency to determine if that
    # frequency amount has any members
    # if so append to output array
    # upon insert update both hashmaps
    # upon delete update both hashmaps

    # Time: O(q) where q is number of queries

    # Space: O(n + c) where n is number of distinct items and c is num
    # distinct counts

    # Edge cases
    # None I can think of, empty queries I guess. Handled below.
    # Bad input (handled in problem statement constraints)

    output = []

    num_frequency = {}
    frequency_frequency = {}

    for idx, query in enumerate(queries):

        # if idx % 100 == 0:
        #     print("Completed {} queries.".format(idx))

        instruction, value = query

        if instruction == 1:
            # add to both hashmaps
            prev_value = num_frequency.get(value, 0)
            num_frequency[value] = prev_value + 1

            # increment new frequency_frequency value
            frequency_frequency[num_frequency[value]] = (
                frequency_frequency.get(num_frequency[value], 0) + 1
            )
            # decrement from old frequency_frequency value if existed
            if frequency_frequency.get(prev_value, 0) > 0:
                frequency_frequency[prev_value] -= 1

        elif instruction == 2:
            # remove from both hashmaps
            freq_to_decrement = num_frequency.get(value, 0)
            if freq_to_decrement > 0:
                num_frequency[value] -= 1

                # decrement current frequency_frequency value
                if frequency_frequency.get(freq_to_decrement, 0) > 0:
                    frequency_frequency[freq_to_decrement] -= 1
                # Increment new frequency value

                frequency_frequency[num_frequency[value]] = (
                    frequency_frequency.get(num_frequency[value], 0) + 1
                )


        elif instruction == 3:
            if frequency_frequency.get(value, 0) > 0:
                output.append(1)
            else:
                output.append(0)

    return output


import unittest

class TestFreqQuery(unittest.TestCase):


    def test_testcase_4(self):

        output_file = "output_case_4_Frequency_Queries_MEDIUM.txt"
        input_file = "input_case_4_Frequency_Queries_MEDIUM.txt"

        with open(input_file) as infile:
            q = infile.readline()
            q = int(q.strip())

            queries = []

            for _ in range(q):
                queries.append(list(map(int, infile.readline().rstrip().split())))

        desired_answer = []
        with open(output_file) as outfile:
            for _ in range(q):
                s = outfile.readline()
                if s:
                    desired_answer.append(int(s))


        self.assertEqual(desired_answer, freqQuery(queries))


    def test_testcase_7(self):

        output_file = "output_case_7_Frequency_Queries_MEDIUM.txt"
        input_file = "input_case_7_Frequency_Queries_MEDIUM.txt"

        # 100,000 queries!!!

        with open(input_file) as infile:
            q = infile.readline()
            q = int(q.strip())

            queries = []

            for _ in range(q):
                queries.append(list(map(int, infile.readline().rstrip().split())))

        desired_answer = []
        with open(output_file) as outfile:
            for _ in range(q):
                s = outfile.readline()
                if s:
                    desired_answer.append(int(s))


        self.assertEqual(desired_answer, freqQuery(queries))


    def test_example_1(self):
        sample_input = (
            """1 5
            1 6
            3 2
            1 10
            1 10
            1 6
            2 5
            3 2"""
        ).splitlines()

        queries = []
        for i in range(8):
            queries.append(list(map(int, sample_input[i].rstrip().split())))
        # print("queries for test_example_1:", queries)

        output = [0, 1]

        self.assertEqual(output, freqQuery(queries))






if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # q = int(input().strip())

    # queries = []

    # for _ in range(q):
    #     queries.append(list(map(int, input().rstrip().split())))

    # ans = freqQuery(queries)

    # fptr.write('\n'.join(map(str, ans)))
    # fptr.write('\n')

    # fptr.close()

    unittest.main()

