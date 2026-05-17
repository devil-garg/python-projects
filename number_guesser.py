import random

r = random.randrange(-1,11) # absolute upper bound -> doesnt include upper bound
r1 =random.randrange(12) # starts with zero
r2=  random.randrange(-9,15,3) #steps of 3
r3= random.randint(-5,11) # include upper bound

top_of_range = input("Provide the max number in the range that you want guess!") # everything that input accepts is a string
if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Pleade provide a number greater than 0 next time")
        quit()
else:
    print("Please provide an integer > 0 next time")
    quit()

random_number = random.randint(0,top_of_range) #always provide lower bound

guesses_allowed = 50

while True:
    user_guess = input("Please make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please provide an integer > 0 next time")
        continue

    if user_guess == random_number:
        print("You got it!")
        print("You have gt in", guesses, "guesses") #autmatically converts data type to string and builds the concatenated string on its own
        break
    elif user_guess > random_number:
        print("you are way above the number")
        guesses-=1
    else:
        print("you are way below the number")
        guesses -= 1
    
    if guesses == 0:
        print("You have run out of you guesses!")
        quit()