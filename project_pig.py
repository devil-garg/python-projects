'''
multiplayer game where you roll a dice and each time you roll a dice its adds up to previous score but ig you score a 1 then you score becomes zero
each player can roll a dice as many time as he can gambling with the possibility of losing his entire score.
Players set a target score and the one who reaches first is the winner
'''

import random

def roll() :
    min_value = 1
    max_value = 6
    roll = random.randint(min_value,max_value)

    return roll

def player_turn(score, playerNo) :
    while score <= max_score :
        choice = input("Would you like to roll? (y or n) ").lower()
        if choice == 'n' :
            return score
        elif choice == 'y' :
            r = roll()
            print("You rolled a", str(r) + "!")
            if  r == 1 :
                score = 0
                print("you score now is",score)
                return score
            else :
                score += r
        else :
            print("Invalid input! Try again")
        
        print("you score now is",score)
        print()
    
    return score

while True:
    playersNo = input("Enter the number of the players (2-4): ")
    if playersNo.isdigit():
        playersNo = int(playersNo)
        if 2 <= playersNo <= 4 :
            break
        else:
            print("Number of players must be between 2-4")
    else:
        print("Invlaid input! Try again")

max_score = 50
players_scores = [0 for i in range(playersNo)] # list comprehension, initialises each index with 0

while True:
    for i in range(playersNo) :
        print()
        print("Player " + str(i+1) + " you turn just started! Your current score is",players_scores[i])
        print()
        score = player_turn(players_scores[i], i)

        if score > max_score :
            players_scores[i] = score
            print("Player",i,"has won the game!")
            print("Scores :", players_scores)
            quit()
        
        players_scores[i] = score
        
