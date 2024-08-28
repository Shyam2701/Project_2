# Guess the number 

import  random
n = random.randint(1,100)
a=0
guesses = 0

while (a != n):
    guesses+=1
    a = int(input("Guesss a number: "))

    if (a>n):
        print("Lower number please.")
    elif(a<n):
        print("Higher number please.")
    else:
        print(f"You have succesfully guesed the number in {guesses} attempt.")

