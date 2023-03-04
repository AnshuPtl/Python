#WAP for random number

import random
num = random.randrange(1,100)
print(num)
print('====================Game Start====================')
i = int(input("Enter First guess:"))

if num == i:
    print("====================You won the Game====================")

else:
    if num<i:
        print("Hint: Think lesser")
    else:
        print("Hint: Think Higher")
    print("Warning: You have 4 chance left")
    print(" ")
    i = int(input("Enter Second guess:"))

    if num == i:
        print("====================You won the Game====================")

    else:
        if num<i:
            print("Hint: Think lesser")
        elif num>i:
            print("Hint: Think Higher")
        print("Warning: You have 3 chance left")
        print(" ")
        
        i = int(input("Enter Third guess:"))
        if num == i:
            print("====================You won the Game====================")

        else:
            if num<i:
                print("Hint: Think lesser")
            elif num>i:
                print("Hint: Think Higher")
            print("Warning: You have 2 chance left")
            print(" ")
            
            i = int(input("Enter Forth guess:"))
            if num == i:
                print("====================You won the Game====================")

            else:
                if num<i:
                    print("Hint: Think lesser")
                else:
                    print("Hint: Think Higher")
                print("Warning: You have 1 chance left")
                print(" ")

                i = int(input("Enter Fifth guess:"))
                if num == i:
                    print("====================You won the Game====================")

                else:
                    print("====================GAME OVER====================")
                    print("The Actual Number is:",num)
    


