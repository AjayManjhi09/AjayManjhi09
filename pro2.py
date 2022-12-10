import random
randNumber = random.randint(1 , 100)
userguess = None
guesses = 0


while(userguess != randNumber):
    userguess = int(input("enter your guess\n"))
    guesses += 1
    if(userguess==randNumber):
        print("your guessed it right")
    else:
        if(userguess>randNumber):
            print("you guessed it wrong! enter a smaller number")
        else:
            print("you guessed it wrong! enter a larger number")

print (f"you gussed the number in {guesses} guesses")
with open ("highscore.txt" , 'r') as f:
    highscore = int(f.read())


if(guesses<highscore):
    print("you have just broken the high score!")
    with open("highscore" , 'w') as f:
        f.write(str(guesses))