import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]
# print(options[0])
# print(options[-2]) # score negative indices

while True:
    user_pick = input("Type Rock/Paper/Scissors or Q to quit ").lower()
    
    if user_pick == "q":
        break
    
    if user_pick not in options:
        continue

    computer_pick = random.randint(0,2)
    computer_pick = options[computer_pick]

    print("Computer picked :",computer_pick)

    if user_pick == "rock" and computer_pick == "scissors" or user_pick == "scissors" and computer_pick == "paper" or user_pick == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1 
    elif user_pick == computer_pick : 
        continue
    else :
        print("You lose!")
        computer_wins += 1
    
print("Score!")
print("User\'s Score :",user_wins)
print("Computer's Score :",computer_wins)
