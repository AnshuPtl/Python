#Write a Python function to insert a string in the middle of a string.

def insert(str1, str2):
  middle = len(str1)//2
  return str1[:middle]+ str2 +str1[middle:]

print(insert('[[]]', 'Java'))
print(insert('{{{}}}', 'Python'))
print(insert('ABDE',"C#"))
