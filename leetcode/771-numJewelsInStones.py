# 771-numJewelsInStones.py

# 771. Jewels and Stones
# Easy

# 1700

# 313

# Favorite

# Share
# You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

# The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so "a" is considered a different type of stone from "A".

# Example 1:

# Input: J = "aA", S = "aAAbbbb"
# Output: 3
# Example 2:

# Input: J = "z", S = "ZZ"
# Output: 0
# Note:

# S and J will consist of letters and have length at most 50.
# The characters in J are distinct.

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        # Get count of stones in S using hashmap
        # then just sum up the ones that are also in J

        stone_counts = {}
        for stone in S:
            stone_counts[stone] = stone_counts.get(stone, 0) + 1

        jewels = 0
        for stone, count in stone_counts.items():
            if stone in J:
                jewels += count

        return jewels

if __name__ == '__main__':
    solution = Solution()

    print("Example 1 Should be 3:", solution.numJewelsInStones("aA", "aAAbbbb"))
    print("Example 2 Should be 0:", solution.numJewelsInStones("z", "ZZ"))


