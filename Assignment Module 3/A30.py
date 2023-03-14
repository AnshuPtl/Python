#WAP to unzip a list of tuples into individual lists.

l = [(1, 2), (3, 4), (5, 6)]
unzipped = list(zip(*l))
print(unzipped) 
