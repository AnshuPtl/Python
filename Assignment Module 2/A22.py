#Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string.

def fun(s):
  if len(s)<2:
    return ''
  else:
    return s[:2]+s[-2:]

print(fun('w3resource'))
print(fun('w3'))
print(fun('w'))


