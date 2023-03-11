#Function with default parameter/argument

def sample (name,age=0,country='india'):
    print("Enter name: ",name)
    print("Enter age: ",age)
    print("Enter country: ",country)
    print("--------------------------------------------")

sample('ABC',20,'japan')
sample('xyz',25)
sample('xcd')


print("==========================================================")
#Function with arbitary parameter/argument

def add(*args):
    sum=()
    for i in args:
        sum=+i
    return sum

print("Addition of tuples:",add(15,8,1,80,60,72,32,3,11,2,52))


print("==========================================================")
#Function with Keyword parameter/argument

def display(**args):
    for i,j in args.items():
        print(i,'=',j)
    print("--------------------Keys--------------------")
    for i in args.keys():
        print(i)
    print("-------------------Values-------------------")
    for i in args.values():
        print(i)

display(v1='Value1',v2='Value2',v3='Value3')
    
