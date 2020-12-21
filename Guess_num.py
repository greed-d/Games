import random

#Setting aside a random number
number = random.randrange(1,100)

chance = 0

while chance < 5 :
    in_num = int(input("Please enter your number between 1-100 : \n"))

    if in_num > 100:
       in_num = input("The number you guessed is out of bounds. Please enter number between 1-100: \n")

    if in_num == number:
        print("\nCongratulations!! You have guessed it correctly\n")
        break
    elif in_num <= number:
        print("\nYour guess is too low. Guess a number higher than : ", in_num)
    else:
        print("\nYour guess is too high. Guess a number lower than : ", in_num)

    chance += 1 
    
if not chance<5:
    print("You Lose!!. The number was :", number)