#WAp to find the repeated items of a tuple.

t=(2, 4, 5, 77, 6, 2, 4, 3, 34, 4, 77, 50, 77, 6, 77, 1, 87)

for i in t:
    if t.count(i)>1:
        print(i,"is repeated",t.count(i),"times")
       
