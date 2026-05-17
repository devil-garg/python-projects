print("Welcome to my computer quiz")

playing = input("Do you want to play the game? ") #accepts the space which means it accepts sentences 

if playing != "yes":
    quit()

print("Okay! Lets play :)")

score = 0 
answer = input("what does CPU stand for? ").lower()
if answer == "central processing unit":
    print("correct!")
    score+=1
else:
    print("incorrect!")

answer = input("what does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("correct!")
    score+=1
else:
    print("incorrect!")

answer = input("what does RAM stand for? ").lower()
if answer == "random access memory":
    print("correct!")
    score+=1
else:
    print("incorrect!")

answer = input("what does PSU stand for? ").lower()
if answer == "power supply unit":
    print("correct!")
    score+=1
else:
    print("incorrect!")

print("You have score " + str(score) + " questions correct!")