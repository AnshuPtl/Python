#Write a Python program to count the occurrences of each word in a given sentence

def count(s):
  
  words = s.split()
  counts = {}
  for i in words:
    if i in counts:
      counts[i] += 1
    else:
      counts[i] = 1
  return counts


s = "This is a sentence with some words which will have repeated words"
print(count(s))
