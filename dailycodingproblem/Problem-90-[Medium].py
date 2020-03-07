# Problem-90-[Medium].py

# Given an integer n and a list of integers l, write a function that randomly generates a number from 0 to n-1 that isn't in l (uniform).

# 2:25p start

# Assumptions
# random generation has to be uniformly distributed (except for items in l)
# there are available values in n (l does not overlap totally with n)
# n >= 2


# Approach
# 1. use random.randint(0, n-1) to generate random number then check if in l
# Time: O(l) for l integers in l for each n desired Space: O(1)
# 2. same as 1 but convert l to hashset first for O(1) lookups
# Time: O(l) one time, not for each l, space O(l)

# the above two can get stuck if no items exist,
# or take a while if we are unlucky

# 3. create list of items range(n-1) without items in l, then use randint()
# to get an index to this new list
# Time: O(n*l) to create list then O(1) to gen new items Space: O(n)
# 4. same as 3 but convert l to hashset for O(1) lookups so
# Time: O(l + n) Space O(l + n)

# Edge cases
# no available n (all possible vals included in l)
# no overlap of n and l
# l = []
# n = 0
# n = 1
# See assumptions

# Let's try approach 4
from typing import List
import random

def randint_except(n: int, l: List[int]) -> int:
    """Return random integer in range(n) that is not in l."""

    # Approach 4

    # # convert l to hashset
    # l_set = set(l)

    # # create list of available items
    # available = []
    # for num in range(n):
    #     if num not in l_set:
    #         available.append(num)

    # # generate and return random value
    # return available[random.randint(0, len(available) - 1)]

    # Approach 2
    # convert l to hashset
    l_set = set(l)
    while True:
        random_value = random.randint(0, n - 1)
        if random_value not in l_set:
            return random_value



if __name__ == '__main__':

    for i in range(10):
        print(
            randint_except(10, [1, 2, 3, 4])
        )