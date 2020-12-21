#Player 
#Value compare
#Create Players

from random import randint

#Create Players
p = ['rock', 'paper', 'scissors']


#Create computer Player
computer = p[randint(0,2)]

player = False

while player == False:
     
     #Prompt user to enter a value
    player = input("Rock, Paper or scissors? Type rock, paper and scissors! :)")

    while player not in ["rock", "paper", "scissors"]:
        player = input("Invalid input please try again : ")

    if player == computer:
        print("Tie!")
    elif player == 'rock':
        if computer == 'paper':
            print("Paper covers Rock!! Computer wins!!")
        else:
            print("You win !!:)")
    elif player == 'scissors':
        if computer == 'rock':
            print("Rock crushes Scissors!! Computer wins")
        else:
            print("You Won!!")
    elif player == 'paper':
        if computer == 'scissors':
            print("Scissors cut paper!! Compuer wins!!")
        else:
            print("You win")
    else:
        print("Invalid input. Please Try again")
player = False
computer = p[randint(0,2)]