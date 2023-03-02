#Housie Game
import random
l1 = []
for i in range(1,13):
    n = int(input("Enter Num: "))
    l1.append(n)
print(l1)


l2 = l1[:len(l1)//2]
l3 = l1[len(l1)//2:]

for i in range (1,13):
    num=random.choice(l1)

    print("User1:",l2)
    print("User2:",l3)

    print("Lucky Number is:",num)

    if num in l2:
        l2.remove(num)
    else:
        l3.remove(num)

    if len(l2)==0:
        print("==========User1 win the Game==========")
        break
    elif len(l3)==0:
        print("==========User2 win the Game==========")
        break
  
    l1.remove(num)


