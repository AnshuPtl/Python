#Quiz game using dictionary



score = 0
Questions={1:"Q1.What is last date of Febuary in 2023?",
           2:"Q2.What is capital of india?"}
    
answers={1:'28',2:'delhi'}

for a in Questions.values():
    print(a)
    
choice=input("Please choose a question number: ")

if choice in Questions:
    print(Questions[choice])


for i in answers:
    print(i)
    ans=input("Enter your Answer: ")
    if ans==answers[i]:
        print("True")
        score=score+10
        print("Your score is:",score)
    else:
        print("False")
        score=score-5
        print("Your score is:",score)
print("Your Total score is:",score)
