#Quiz game using dictionary

name=input("Enter your name: ")

print('Hello',name)

score = 0
Q1="Q1.What is last date of Febuary in 2023?"
Q2="Q2.What is capital of india?"

answer={Q1:'28',Q2:'Delhi' and 'delhi'}
print(type(answer))

for i in answer:
    print(i)
    ans=input("Enter your Answer: ")
    if ans==answer[i]:
        print("True")
        score=score+10
        print("Your score is:",score)
    else:
        print("False")
        score=score-5
        print("Your score is:",score)
print("Your Total score is:",score)
