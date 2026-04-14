import random

number =random.randint(1,50)

print ("guess the number (1 to 50)")
print ("you have only three chances")

for i in range (3):
    guess = int (input("enter your guess: "))

    if guess == number:
        print ("congratulation ! you win ")
        break 
    elif guess>number:
        print ("too high")
    else :
        print ("too low ")

else:
    print ("you lost !better luck next time ")
    print  ("Number was :", number )
