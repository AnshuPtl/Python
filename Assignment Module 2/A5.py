#What is the purpose continue statement in python?

#The continue statement in Python is used to skip the rest of the code inside a loop for the current iteration only, and continue with the next iteration. The continue statement is useful when you want to ignore some specific condition in a loop.

for i in range(1,11):
    if i ==4:
        continue

    print(i)
