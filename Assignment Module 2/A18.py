#Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead if the string length of the given string is less than 3, leave it unchanged

def add(s):
  if len(s)<3:
    return s
  else:
    if s.endswith('ing'):
      return s+'ly'
    else:
      return s+'ing'

print(add('play'))
print(add('sing'))
print(add('by'))
