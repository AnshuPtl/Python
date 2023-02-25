#Jumping Statement

#1. Break

for i in range(1,11):
    if i == 5:
        break
    print(i)

print("-------------------------------------------")

#2. Continue

for i in range(1,11):
    if i == 5:
        continue
    print(i)

print("-------------------------------------------")

#3. Pass

for i in range(1,11):
    if i == 5:
        pass
    print(i)
