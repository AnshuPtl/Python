#Write a Python function to reverses a string if its length is a multiple of 4

def reverse(s):
  if len(s)%4==0:
    return s[::-1]
  else:
    return s

print(reverse('abcd'))
print(reverse('uvwxyz'))
