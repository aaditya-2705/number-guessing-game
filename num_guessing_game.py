#NUMBER GUESSING GAME

import random                          

def play_game() :
    rand_num=random.randint(1,100)
    attempts=1
    print("Welcome to the number guessing game!")
    print("Instructions:\nThe computer will randomly take an integer from 1 to 100 and you have to guess it.")

    try:
        guessed_num=int(input("Guess a number from 1 to 100: "))
        while guessed_num!=rand_num :
            attempts+=1
            if guessed_num>rand_num :
                print("Your guess is higher than the correct number.")
            else :
                print("Your guess is lower than the correct number.")
            guessed_num=int(input("Guess again: "))
        print("Congrats! You've guessed it right in "+str(attempts)+" attempts")
    
    except ValueError :
        print("Please enter an integer!")

while True:
    play_game()
    choice=input("Do you want to play again?\nEnter 'y' to play again or any other key to exit: ").lower()
    if choice!='y' :
        print("Thanks for playing!")
        break