#Write a Python program to count occurrences of a substring in a string

s = 'ABC DFG  ABCHIJ KLABCM NOP QARS'
sb = 'ABC'
r = 0
sub= len(sb)
for i in range(len(s)):
    if s[i:i+sub] == sb:
        r += 1
print (r)
