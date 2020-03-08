# word_count_engine.py
# https://www.pramp.com/challenge/W5EJq2Jld3t2ny9jyZXG

# Original submission

# def word_count_engine(document):

#   # Assumptions
#   # Given strings
#   # english, strip all punctuation
#   # bounded by whitespace
#   # sort by original order
#   # case insensitive
#   # return string counts ["practice", "3"]

#   # Approach
#   # split doc by " " -> list of words
#   # iterate through each word
#   # process (remove punctuation, change to lowercase)
#   # can't use hashmap to store counts bc we need order preserved
#   # append new word with "1" count to end
#   # to increment then I need to iterate thru output

#   # store counts in hashmap
#   # iterate through list_of_words
#   # build my output from list of words
#   # iterate through list of words add [word, count] by popping from hashmap

#   # how to keep sorted
#   # ["practice", "3"], ["perfect", "2"],
#   # ["makes", "1"], ["youll", "1"], ["only", "1"],
#   # ["get", "1"], ["by", "1"], ["just", "1"]

#   # Priority queue (Max Heap) (count, word) - order by count
#   # When equal counts iterate through list_of_words to find order
#   # create ordered array of unique words [all unique words] ordered by insertion from list_of_words
#   # Time: O(N*N)

#   # Hint: think about bucket sort
#   # build histogram
#   '''
#   [
#     [word1, word2] # index = count
#     [word3, word4] # index = count
#   ]
#   '''
#   # iterate through this structure to get answer
#   # [minoccu, max_occur]

#   # Time: O(N) time N = num words in document
#   # Space: O(N) hashmap O(N) list_of_words O(N) output

#   # Edge Cases
#   # document = ""
#   # document all punctuation
#   # document isn't string

#   list_of_words_unprocessed = document.split(' ')
#   list_of_processed_words = []
#   for word in list_of_words_unprocessed:
#     word = word.lower().strip()
#     for char in word:
#       temp_word = []
#       if char in 'abcdefghijklmnopqrstuvwxyz':
#         temp_word.append(char)

#     list_of_processed_words.append(str(temp_word))


#   # store counts in hashmap
#   word_counts = {}
#   max_count = 0
#   for word in list_of_processed_words:
#     word_counts[word] = word_counts.get(word, 0) + 1
#     if word_counts[word] > max_count:
#       max_count = word_counts[word]


#   ordered_counts = [[None]] * (max_count + 1)

#   #for word, count in word_counts.items():
#   for word in list_of_processed_words:
#     if word_counts.get(word):
#       ordered_counts[word_counts[word]].append(word)
#       word_counts.pop(word)

#   # build output
#   ouput = []
#   for idx, count in enumerate(ordered_counts):
#     if count != [None]:
#       for word in count:
#         output.append([word, str(idx)])

#   return output




# Debugged


def word_count_engine(document):

  # Assumptions
  # Given strings
  # english, strip all punctuation
  # bounded by whitespace
  # sort by original order
  # case insensitive
  # return string counts ["practice", "3"]

  # Approach
  # split doc by " " -> list of words
  # iterate through each word
  # process (remove punctuation, change to lowercase)
  # can't use hashmap to store counts bc we need order preserved
  # append new word with "1" count to end
  # to increment then I need to iterate thru output

  # store counts in hashmap
  # iterate through list_of_words
  # build my output from list of words
  # iterate through list of words add [word, count] by popping from hashmap

  # how to keep sorted
  # ["practice", "3"], ["perfect", "2"],
  # ["makes", "1"], ["youll", "1"], ["only", "1"],
  # ["get", "1"], ["by", "1"], ["just", "1"]

  # Priority queue (Max Heap) (count, word) - order by count
  # When equal counts iterate through list_of_words to find order
  # create ordered array of unique words [all unique words] ordered by insertion from list_of_words
  # Time: O(N*N)

  # Hint: think about bucket sort
  # build histogram
  '''
  [
    [word1, word2] # index = count
    [word3, word4] # index = count
  ]
  '''
  # iterate through this structure to get answer
  # [minoccu, max_occur]

  # Time: O(N) time N = num words in document
  # Space: O(N) hashmap O(N) list_of_words O(N) output

  # Edge Cases
  # document = ""
  # document all punctuation
  # document isn't string

  list_of_words_unprocessed = document.split(' ')
  list_of_processed_words = []
  for word in list_of_words_unprocessed:
    word = word.lower().strip()
    temp_word = []
    for char in word:
      if char in 'abcdefghijklmnopqrstuvwxyz':
        temp_word.append(char)

    if len(temp_word) > 0:
      list_of_processed_words.append("".join(temp_word))


  # store counts in hashmap
  word_counts = {}
  max_count = 0
  for word in list_of_processed_words:
    word_counts[word] = word_counts.get(word, 0) + 1
    if word_counts[word] > max_count:
      max_count = word_counts[word]


  ordered_counts = [[]] * (max_count + 1)

  #for word, count in word_counts.items():
  for word in list_of_processed_words:
    if word_counts.get(word):
      ordered_counts[word_counts[word]] = [word] + ordered_counts[word_counts[word]]
      word_counts.pop(word)


  # build output
  output = []
  for idx, count in enumerate(ordered_counts):
    if count != [None]:
      for word in count:
        output = [[word, str(idx)]] + output

  return output

if __name__ == '__main__':
  document = "Practice makes perfect. you'll only get Perfect by practice. just practice!"
  print(word_count_engine(document))

  document = "Practice makes perfect, you'll get perfecT by practice. just practice! just just just!!"
  print(word_count_engine(document))

  document = "Look If you had One shot, Or one opportunity, To seize everything you ever wanted, In one moment, Would you capture it, Or just let it slip?"
  print(word_count_engine(document))
