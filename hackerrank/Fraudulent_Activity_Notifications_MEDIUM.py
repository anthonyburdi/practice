# Fraudulent_Activity_Notifications_MEDIUM.py

# https://www.hackerrank.com/challenges/fraudulent-activity-notifications/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=sorting

# HackerLand National Bank has a simple policy for warning clients about possible fraudulent account activity. If the amount spent by a client on a particular day is greater than or equal to  the client's median spending for a trailing number of days, they send the client a notification about potential fraud. The bank doesn't send the client any notifications until they have at least that trailing number of prior days' transaction data.

# Given the number of trailing days  and a client's total daily expenditures for a period of  days, find and print the number of times the client will receive a notification over all  days.

# For example,  and . On the first three days, they just collect spending data. At day , we have trailing expenditures of . The median is  and the day's expenditure is . Because , there will be a notice. The next day, our trailing expenditures are  and the expenditures are . This is less than  so no notice will be sent. Over the period, there was one notice sent.

# Note: The median of a list of numbers can be found by arranging all the numbers from smallest to greatest. If there is an odd number of numbers, the middle one is picked. If there is an even number of numbers, median is then defined to be the average of the two middle values. (Wikipedia)

# Function Description

# Complete the function activityNotifications in the editor below. It must return an integer representing the number of client notifications.

# activityNotifications has the following parameter(s):

# expenditure: an array of integers representing daily expenditures
# d: an integer, the lookback days for median spending
# Input Format

# The first line contains two space-separated integers  and , the number of days of transaction data, and the number of trailing days' data used to calculate median spending.
# The second line contains  space-separated non-negative integers where each integer  denotes .

# Constraints

# Output Format

# Print an integer denoting the total number of times the client receives a notification over a period of  days.

# Sample Input 0

# 9 5
# 2 3 4 2 3 6 8 4 5
# Sample Output 0

# 2
# Explanation 0

# We must determine the total number of  the client receives over a period of  days. For the first five days, the customer receives no notifications because the bank has insufficient transaction data: .

# On the sixth day, the bank has  days of prior transaction data, , and  dollars. The client spends  dollars, which triggers a notification because : .

# On the seventh day, the bank has  days of prior transaction data, , and  dollars. The client spends  dollars, which triggers a notification because : .

# On the eighth day, the bank has  days of prior transaction data, , and  dollars. The client spends  dollars, which does not trigger a notification because : .

# On the ninth day, the bank has  days of prior transaction data, , and a transaction median of  dollars. The client spends  dollars, which does not trigger a notification because : .

# Sample Input 1

# 5 4
# 1 2 3 4 4
# Sample Output 1

# 0
# There are  days of data required so the first day a notice might go out is day . Our trailing expenditures are  with a median of  The client spends  which is less than  so no notification is sent.

'''
# Assumptions

# Approach

1. create new slice of the previous d days, sort to find the median and then
check the next day.
Do this for each day starting with index d until the end of the list
If the notification should go out (curr >= 2*median) then add 1 to running sum
Time: O(n) for the traversal, O(dlogd) for the sort. Total O(n*d*logd)
Space: O(d) since we keep another array of size d. Perhaps more if we use
a sorting algorithm that is not in-place. Use maybe heapsort

2. min and max heap for finding median. Still O(d) space but we can reduce
the sorting down to O(logd) since we are just heapifying each additional
daily total. No need for sorting.
We take the average of the min and max heap top values for the median
and insert into the appropriate heap. If the heaps are out of balance then we
rebalance (within 1 element) before taking median. Whichever heap is larger
then holds the median at it's root.
We insert a new item into the max heap if it is less than or equal to the root
value of the max heap
We insert a new item into the min heap if it is greater or equal to the root
value of the min heap

3. Since expenduture is <= 200 we can do a bucket or radix sort in O(n) time

Since this is a sorting problem, let's do option 1 with bucket sort.

Performance is not good enough, looks like I have to do 3 but with a sliding
window (remove old value and add new value) rather than create a new
window each time.


# Edge Cases
len(expenditure) <= d

    # Steps
    # 1. start iterating at 0 and append each new value to a temp array
    # 2. when we reach d then remove oldest value from temp array (maybe can use a deque to make faster)
    # 3. find the median of the items in the current queue, using counting sort
    # 4. compare to half of the next item and increment activity notifications if greater

    # nevermind the above
    # Change some steps:
    # just add directly to counting array and remove from that array as well. Then constant space also.

    # normally import goes at the top of a file
'''




#!/bin/python3

import math
import os
import random
import re
import sys

def find_median(counts):
    """Find the median of a counted set of values."""
    
    even = sum(counts) % 2 == 0
    first_count = (sum(counts) // 2)
    mid_count = (sum(counts) // 2) + 1

    # if even length, median equuals average(index_first_count, index_mid_count)
    # if odd length, median equals index_mid_count

    index_first_count = -1
    index_mid_count = -1

    # find indices
    i = 0
    running_sum = 0
    while i < len(counts):
        running_sum += counts[i]

        if running_sum >= mid_count and index_mid_count == -1:
            index_mid_count = i
            if not even:
                return index_mid_count

        if running_sum >= first_count and index_first_count == -1:
            index_first_count = i

        if even and index_first_count != -1 and index_mid_count != -1:
            return (index_first_count + index_mid_count) / 2

        i += 1


# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):

    # Edge cases
    if len(expenditure) <= d:
        return 0


    notifications = 0
    counts = [0] * 201 # Since expenditures can be up to 200 from 0
    f = 0
    b = 0

    while f < len(expenditure):

        if f >= d:
            median = find_median(counts)

            if float(expenditure[f]) >= (2.0 * median):
                notifications += 1

            counts[expenditure[b]] -= 1
            b += 1


        counts[expenditure[f]] += 1
        f += 1

    return notifications


import unittest

class TestActivityNotifications(unittest.TestCase):

    def test_given_examples(self):

        d = 5
        expenditure = [2, 3, 4, 2, 3, 6, 8, 4, 5]
        self.assertEqual(2, activityNotifications(expenditure, d))
        # [1,2,3,4,5,6,7]
        # [0,1,2,3,4,5,6]

        # f = 7
        # d = 5
        # b = 2
        # median = 4
        # len(expenditure) = 9
        # notifications = 2
        # expenditure = [2, 3, 4, 2, 3, 6, 8, 4, 5]
        # expenditure = [0, 1, 2, 3, 4, 5, 6, 7, 8] (indices)
        # counts = [0,0,1,1,1,0,1,0,1]
        # counts = [0,1,2,3,4,5,6,7,8] (indices)


    def test_given_examples_2(self):

        d = 3
        expenditure = [10, 20, 30, 40, 50]
        self.assertEqual(1, activityNotifications(expenditure, d))
        # '''
        # expenditure = [10, 20, 30, 40, 50]
        # expenditure = [0,  1,  2,  3,  4] (indices)
        # len 5
        # d = 3
        # f = 4
        # b = 1
        # expenditure[f] = 40
        # median = 20
        # counts = [0,...1, 1, 1, 0]
        # counts = [10,..20,30,40,50]
        # notifications = 1
        # '''


    def test_median(self):

        c = [0,0,1,0,0,0,0,0,0]
        self.assertEqual(2, find_median(c))

        c = [0,0,1,1,1,0,0,0,0]
        self.assertEqual(3, find_median(c))

        c = [0,0,2,1,1,0,0,0,0]
        self.assertEqual(2.5, find_median(c))

        c = [0,0,2,2,1,0,0,0,0]
        self.assertEqual(3, find_median(c))

        c = [0,0,1,2,1,0,1,0,0]
        self.assertEqual(3, find_median(c))

        c = [0,0,1,1,1,0,1,0,1]
        self.assertEqual(4, find_median(c))


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # nd = input().split()

    # n = int(nd[0])

    # d = int(nd[1])

    # expenditure = list(map(int, input().rstrip().split()))

    # result = activityNotifications(expenditure, d)

    # fptr.write(str(result) + '\n')

    # fptr.close()

    unittest.main()











