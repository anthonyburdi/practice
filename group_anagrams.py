"""Group anagrams question."""
# https://leetcode.com/problems/group-anagrams/description/
# Given an array of strings, group anagrams together.

# For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Return:

# [
#   ["ate", "eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
# Note: All inputs will be in lower-case.
import pprint


def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    output = []

    word_letter_counts = []

    for idx, word in enumerate(strs):
        word_dict = {}
        for letter in word:
            if word_dict.get(letter):
                word_dict[letter] += 1
            else:
                word_dict[letter] = 1

        word_letter_counts.append(word_dict)

    while word_letter_counts:
        anagram_list = []

        word_to_check = word_letter_counts.pop(0)
        word = strs.pop(0)
        anagram_list.append(word)

        for idx, word_letter_count in enumerate(word_letter_counts):
            if word_to_check == word_letter_count:
                # add the matching word to the anagram list and remove
                # from input and word_letter_counts
                anagram_list.append(strs.pop(idx))
                word_letter_counts.pop(idx)

        anagram_list.sort()
        output.append(anagram_list)
    return output

input_words = ["eat", "tea", "tan", "ate", "nat", "bat"]
print 'input_words anagrams: '
print input_words

pp = pprint.PrettyPrinter(indent=4)
print 'Output anagrams:'
pp.pprint(groupAnagrams(input_words))


