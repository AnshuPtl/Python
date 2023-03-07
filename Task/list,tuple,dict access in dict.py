#Applying list,tuple and dictionary as value inside a dictionary

d = {
    1:{'o':"Orange",'a':'Apple'},
    2:('t1','t2'),
    'num':[1,2,3,4,5,6,7]
    }

print("Access List elements from dictionary:",d['num'][4])
print('Access Tuple elements from dictionary:',d[2][1])
print("Access Dictionary elements from dictionary:",d[1]['a'])
