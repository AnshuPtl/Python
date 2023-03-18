#Anonymous Function: Lambda

def myfun(n1):
    return lambda p:p+n1

var = myfun(2)

print (var (2))
