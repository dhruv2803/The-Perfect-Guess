import random
randNumber=random.randint(1,100)
guess=0
userGuess=None
while userGuess!=randNumber:
    userGuess=int(input("Enter your guess: "))
    guess+=1
    if userGuess==randNumber:
        print(f"Your guess is correct. That number is {userGuess}")
    else:
        if userGuess<randNumber:
            print("Guess is incorrect. Please enter larger number")
        else:
            print("Guess is incorrect. Please enter smaller number")

print(f"Number of gusses taken by you is {guess}")

with open("LowestNumberOfStep.txt") as f:
    lowScore=f.read()
    
if lowScore == '' or int(lowScore)>guess:
    print("Your have guessed number in lowest number of step, Your score is saved")
    with open("LowestNumberOfStep.txt",'w') as f:
        f.write(str(guess))

