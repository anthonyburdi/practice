# Hash_Tables_Ice_Cream_Parlor_MEDIUM.py

# https://www.hackerrank.com/challenges/ctci-ice-cream-parlor/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=search

# Each time Sunny and Johnny take a trip to the Ice Cream Parlor, they pool their money to buy ice cream. On any given day, the parlor offers a line of flavors. Each flavor has a cost associated with it.

# Given the value of  and the  of each flavor for  trips to the Ice Cream Parlor, help Sunny and Johnny choose two distinct flavors such that they spend their entire pool of money during each visit. ID numbers are the 1- based index number associated with a . For each trip to the parlor, print the ID numbers for the two types of ice cream that Sunny and Johnny purchase as two space-separated integers on a new line. You must print the smaller ID first and the larger ID second.

# For example, there are  flavors having . Together they have  to spend. They would purchase flavor ID's  and  for a cost of . Use  based indexing for your response.

# Note:

# Two ice creams having unique IDs  and  may have the same cost (i.e., ).
# There will always be a unique solution.
# Function Description

# Complete the function whatFlavors in the editor below. It must determine the two flavors they will purchase and print them as two space-separated integers on a line.

# whatFlavors has the following parameter(s):

# cost: an array of integers representing price for a flavor
# money: an integer representing the amount of money they have to spend
# Input Format

# The first line contains an integer, , the number of trips to the ice cream parlor.

# Each of the next  sets of  lines is as follows:

# The first line contains .
# The second line contains an integer, , the size of the array .
# The third line contains  space-separated integers denoting the .
# Constraints

# Output Format

# Print two space-separated integers denoting the respective indices for the two distinct flavors they choose to purchase in ascending order. Recall that each ice cream flavor has a unique ID number in the inclusive range from  to .

# Sample Input

# 2
# 4
# 5
# 1 4 5 3 2
# 4
# 4
# 2 2 4 3
# Sample Output

# 1 4
# 1 2
# Explanation

# Sunny and Johnny make the following two trips to the parlor:

# The first time, they pool together  dollars. There are five flavors available that day and flavors  and  have a total cost of .
# The second time, they pool together  dollars. There are four flavors available that day and flavors  and  have a total cost of .


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the whatFlavors function below.
def whatFlavors(cost, money):
    # Assumptions
    # see problem statement

    # Approach, Complexity & Tradeoffs
    # brute force use two for loops O(N^2)
    # add costs to hash table as keys with values of index + 1 O(N)
    # if collisions add to a list
    # for each cost, subtract from money and look for that cost in hash table
    # if it exists take index of current + 1 and value from hash table.
    # if the value in hash  table  is a list then check for an item not
    # equal to current + 1 O(N)
    # Total time complexity = O(N)
    # Total space complexity = O(N)

    # Potential improvements
    # maybe simpler, maybe in  place solution

    # Edge Cases
    # Equal cost flavors
    # see constraints and problem statement

    # Initialize
    cost_locations = {}

    # create hash table
    for i, c in enumerate(cost):
        if cost_locations.get(c):
            if type(cost_locations[c]) == list:
                cost_locations[c].append(i + 1)
            elif type(cost_locations[c]) == int:
                cost_locations[c] = [cost_locations[c], i + 1]
        else:
            cost_locations[c] = i + 1

    # iterate through costs
    for i, c in enumerate(cost):
        pair_cost = money - c
        if pair_cost in cost_locations:

            # don't take duplicate
            if cost_locations[pair_cost] == i + 1:
                continue

            if type(cost_locations[pair_cost]) == int:
                ordered_indices = sorted([
                    cost_locations[pair_cost],
                    i + 1
                ])
                print("{} {}".format(ordered_indices[0], ordered_indices[1]))
                return

            if type(cost_locations[pair_cost]) == list:
                desired_index = None

                # Don't take duplicates:
                for other_index in cost_locations[pair_cost]:
                    if other_index != i + 1:
                        desired_index = other_index
                        break

                ordered_indices = sorted([
                    desired_index,
                    i + 1
                ])
                print("{} {}".format(ordered_indices[0], ordered_indices[1]))
                return



if __name__ == '__main__':
    # t = int(input())

    # for t_itr in range(t):
    #     money = int(input())

    #     n = int(input())

    #     cost = list(map(int, input().rstrip().split()))

    #     whatFlavors(cost, money)

    money = 8

    cost = [4, 3, 2, 5, 7]

    print("Should be 2 4:")
    whatFlavors(cost, money)




