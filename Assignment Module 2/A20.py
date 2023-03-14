#Write a Python function that takes a list of words and returns the length of the longest one.

def longest_word(words):
  max_len = 0
  longest_word = None
  for i in words:
    if len(i) > max_len:
      max_len = len(i)
      longest_word = i
  return longest_word

print(longest_word(['hello', 'world', 'Python', 'programming']))
