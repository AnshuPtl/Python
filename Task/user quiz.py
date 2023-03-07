#user inputed questions quiz
questions = {
    '1':"What is the name of this programming language?",
    '2':"Who was one of the founders of Apple?",
    '3':"What is the term for creating machines that can think like humans?",
    '4':"What is the name of the digital currency that uses cryptography?"
}


correct_ans = {
    '1':"python",
    '2':"steve jobs",
    '3':"artificial intelligence",
    '4':"bitcoin"
}


score = 0

for i in range(len(questions)):
    user=input("Enter a Number of question:")
    if user in questions:
        print(questions[user])
        ans = input("Your answer: ")
        
        if ans==correct_ans[user]:
            print("Correct!")
            score += 10 
            print("Your score is:",score)
        else:
            print("Incorrect!")
            score -= 5
            print("Your score is:",score)
            
        del questions[user]

    else:
        print("question not found")
    
print(f"Your final score is {score} out of {len(questions)*10}.")
