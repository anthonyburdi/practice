# Anonymous_Love_Letter.py

# Anonymous Love Letter
# You have written an anonymous love letter and you don’t want your handwriting to be recognized. Since you don’t have a printer within reach, you are trying to write this letter by copying and pasting characters from a newspaper.

# Given a string L representing the letter and a string N representing the newspaper, return true if the L can be written entirely from N and false otherwise. The letter includes only ascii characters.


# Assumptions
# case sensitive
# all data fits on a single machine
# include punctuation but not spaces

# Approach
# Make character counts of L and N
# make sure no characters in L are not
# sufficiently represented in N
# O(L + N) for creating the char_counts and reviewing
# (in time & constant in space since finite num of chars)

# Edge Cases
# null inputs

def can_letter_be_made(L, N):

  if not N: return False

  letter_counts = {}
  newspaper_counts = {}

  for char in L:
    if char is not " ":
      letter_counts[char] = letter_counts.get(char, 0) + 1

  for char in N:
    if char is not " ":
      newspaper_counts[char] = newspaper_counts.get(char, 0) + 1


  for char, count in letter_counts:
    if newspaper_counts.get(char, 0) < count:
      return False

  return True
