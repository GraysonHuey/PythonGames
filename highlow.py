#import the necessary packages and modules 
from random import randint
from tkinter import Variable
from turtle import goto

def game():
    value=randint(1,100)
    count=0
    global wins
    wins=0
    
    print("I have chosen a random number from 1-100")
    while count!=10:
        guess = int(input("Make your guess:"))
        
        if guess>value:
            print("Oops, the number I chose is lower than this, try again!")
            count+=1
        elif guess<value:
            print("Uh oh, the number I chose is higher than this, try again!")
            count+=1
        else:
            print("Excellent job! You guessed correctly!")
            wins += 1
            print("Now you have " +str(wins), "win(s)!")
            replay()
    print("I chose %i!" %value)
    replay()

def replay():
    global wins
    play_again = input("Would you like to play again? y/n: ")
    if play_again == "y":
        game()
    elif play_again == "n":
        print("Thanks for playing!")
        print("You won " +str(wins), "time(s)")
        exit()
    else:
        print("Response invalid!")
    
def main():
    print("*************************WELCOME TO THE HIGHER-LOWER GAME*************************")
    print("Instructions: \n1. The computer will randomly choose a number between 1-100\n2. Then, It will ask you to guess which number it chose")
    print("3.You will then make your guess and the computer will tell you if your guess was higher, lower or equal to its choice\n4. You will get ten chances! \n5Good Luck!")
    response = input("Do you wish to play? Respond with y/n: ")
    if response =="y":
        game()
    elif response =="n":
        exit()
    else:
        print("Response invalid!")

main()