#Write a Python function that takes two lists and returns true if they have at least one common member.

list1=[5,4,9,3,7,8]
list2=[8,20,70,3,5,7]

 
for element in list1:
    if element in list2:
      return True
 
  return False

    


