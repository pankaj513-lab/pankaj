import random
word =random.choice([ "python","computer ","programming ", "algorithm","keyword "])
guessed=""
chances= 7
print ("Welcome to the Hangman Game ")

while chances > 0:
    display= ""
    
    for letter in word :
        if letter in guessed:
            display+=letter
        else:
            display+="_"
    print ("\nword :", display)

    if display ==word:
        print ("🥳🎉you win ! ")
        break
    
    guess = input ("guess a letter :").lower()

    if guess in guessed:
        print ("⚠️ already guessed !")
        continue
    guessed += guess 

    if guess not in word :
        chances -=1
        print("wrong guess ")
        print ("chances left", chances )

if chances==0:
    print ("\n💀 you lost")
    print ("word was :",word)
