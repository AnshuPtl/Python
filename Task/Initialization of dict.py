#Initialization of Dictionary

dict_ex1=dict()
dict_ex2=()

d1={'k1':12,'k2':123,'msg':"Hello"}
d2=dict(Name='abc',Name2='pasd',Name3="poi")

print(d1)
print(d2)

#Dictionary Access

print(d1['k2'])

#get method
print(d1.get('msg'))


#copy & update dictionary

dict1={2,'rg',80}
dict2={1,5,8,'sd'}

dict1:dict2.copy()
print("dict1 copy from d2=",dict1)
dict1.update (d1)
print("dict1 update from d2=",dict1)

