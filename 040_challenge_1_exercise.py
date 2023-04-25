# Video alternative: https://youtu.be/qDWyR0XpJtQ&t=1295s

from lib.helpers import check_that_these_are_equal

# Now it's your turn.

# Note that the exercise will be (a little) less challenging
# than the example.

# Write a function that takes a list of words and returns a
# report of all the words that are longer than 10 characters
# but don't contain a hyphen. If those words are longer than
# 15 characters, then they should be shortened to 15
# characters and have an ellipsis (...) added to the end.

# For example, if the input is:
# [
#   'hello',
#   'nonbiological',
#   'Kay',
#   'this-is-a-long-word',
#   'antidisestablishmentarianism'
# ]
# then the output should be:
# "These words are quite long: nonbiological, antidisestablis..."

# @TASK: Complete this exercise.

print("")
print("Function: report_long_words")

def report_long_words(words):
  filtered_words= filtered_words_by_length(words)
  if filtered_words == [] :
    return "These words are quite long: "
  else:
    long_words=long_words_list(filtered_words)
    long_words_result = final_result(long_words)
 
    return long_words_result

def final_result (words):
  result="These words are quite long:"
  for item in words:
    if item == words[-1]:
      result += f" {item}"
    else:
      result += f" {item},"    
  return result
    
def long_words_list(words):
  long_words=[]
  for item in words:
    if len(item) > 15:
      words = f"{item[0:15]}..."
      long_words.append(words)
    else:
      long_words.append(item)
  return long_words

def filtered_words_by_length(words):
  filtered_word=[]
  for item in words:
    if len(item) >=10 and "-" not in item:
      filtered_word.append(item)
  return filtered_word
  
  

check_that_these_are_equal(
  report_long_words([
    'hello',
    'nonbiological',
    'Kay',
    'this-is-a-long-word',
    'antidisestablishmentarianism'
  ]),
  "These words are quite long: nonbiological, antidisestablis..."
)

check_that_these_are_equal(
  report_long_words([
    'cat',
    'dog',
    'rhinosaurus',
    'rhinosaurus-rex',
    'frog'
  ]),
  "These words are quite long: rhinosaurus"
)

check_that_these_are_equal(
  report_long_words([
    'cat'
  ]),
  "These words are quite long: "
)

# Once you're done, move on to 041_challenge_2_example.py
