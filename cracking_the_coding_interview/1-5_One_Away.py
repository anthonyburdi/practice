# 1-5_One_Away.py

# Is one string one edit away from another

# Assumptions
# all lowercase (or case doesn't matter) a-z ascii only
# strings fit on a single computer

# Approach
# Create arrays of char counts and populate
# subtract one array from the other element  by element
# (never going negative)
# if the sum of the resulting array > 1 return false else true
# nope doesn't work have  to do reciprocal too
# Let's just create a dict counter and remove items
# Also need to check lengths aren't different by more than 1

# these approaches are O(N) time where N is length of one of the strings
# and also O(1) space since a count array is constant space

# we could also do this in place by moving pointers around and checking as in
# the solution...

# examples
# pale, bale =
# assume 1's in proper position: [0,1,1,1,1,0]  and  [1,1,1,1,0,0]
# resulting  array of arr1-arr2  = [0,0,0,0,1,0] true
# pale, bake =
# bpalek [0,1,1,1,1,0] [1,0,1,0,1,1]
# resulting arr of arr1-arr2 = [0,1,0,1,0,0] = 2 false
# pale, ple =
# pale [1,1,1,1] [1,0,1,1]
# result = [0,1,0,0] = 1 true
# pales, pale = pales [1,1,1,1,1] [1,1,1,1,0] => [0,0,0,0,1] => 1 true

def one_away(s1:str, s2:str):
    """Check if s1 and s2 are only one edit away (insert, remove, replace)."""

    # s1_counts = [0] * 26
    # s2_counts = [0] * 26

    # for char in s1:
    #     char_idx = ord(char) - ord("a")
    #     s1_counts[char_idx] += 1

    # for char in s2:
    #     char_idx = ord(char) - ord("a")
    #     s2_counts[char_idx] += 1

    # print(s1_counts, s2_counts)

    # edits = 0

    # for i in range(len(s1_counts)):
    #     if edits > 1:
    #         return False
    #     else:
    #         diff = abs(s1_counts[i] - s2_counts[i])
    #         # if diff < 0:
    #         #     diff = 0
    #         edits += diff

    # if edits == 0 or edits == 1:
    #     return True
    # else:
    #     return False

    def get_char_counts(s:str) -> dict:
        """return dict of char counts."""
        counts = {}
        for c in s:
            counts[c] = counts.get(c, 0) + 1
        return counts

    s1_counts = get_char_counts(s1)
    s2_counts = get_char_counts(s2)

    length_diff = abs(len(s1) - len(s2))
    if length_diff > 1:
        return False

    for char, count in s1_counts.items():
        if s1_counts[char] < s2_counts.get(char, 0):
            s1_counts[char] = 0
        else:
            s1_counts[char] -= s2_counts.get(char, 0)

    edits = sum(s1_counts.values())

    if edits == 0 or edits == 1:
        return True
    else:
        return False


import unittest

class TestOneAway(unittest.TestCase):

    def test_ex1(self):
        s1 = "pale"
        s2 = "ple"
        self.assertTrue(one_away(s1,s2))

    def test_ex2(self):
        s1 = "pales"
        s2 = "pale"
        self.assertTrue(one_away(s1,s2))

    def test_ex3(self):
        s1 = "pale"
        s2 = "bale"
        self.assertTrue(one_away(s1,s2))

    def test_ex4(self):
        s1 = "pale"
        s2 = "bake"
        self.assertFalse(one_away(s1,s2))

    def test_long_example(self):
        s1 = "helloimalongstring"
        s2 = "imanotherstringthatisverylonglonglong"
        self.assertFalse(one_away(s1,s2))

    def test_insert_in_second(self):
        s1 = "ple"
        s2 = "pale"
        self.assertTrue(one_away(s1,s2))

if __name__ == '__main__':
    unittest.main()
