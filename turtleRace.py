import turtle 
import time
import random

WIDTH, HEIGHT = 500, 500
COLORS = ['red', 'green', 'blue', 'orange', 'yellow', 'black', 'cyan','purple', 'pink', 'brown']

def get_racers_their_characteristics(racers) :
    global COLORS
    random.shuffle(COLORS)
    COLORS = COLORS[ :len(racers)]
    spacingx = WIDTH // (len(COLORS) + 1)
    for i in range(len(racers)) :
        racers[i].color(COLORS[i])
        racers[i].shape('turtle')
        racers[i].left(90)
        racers[i].penup()
        racers[i].setpos( -WIDTH // 2 + (i+1) * spacingx, -HEIGHT // 2 + 20)
        racers[i].pendown()
        
    return

def race(racers) :
    while True :
        for index, racer in enumerate(racers) :
            distance = random.randrange(1,10)
            racer.forward(distance)

            x, y = racer.pos()
            if y >= HEIGHT // 2 - 10 :
                return index
            
def get_the_number_of_racers() :
    racers = 0
    while True :
        racers = input('Enter the number of racers (2-10): ')
        if racers.isdigit() :
            racers = int(racers)
        else : 
            print('Input is not numeric! Try Again. ')
            continue

        if 2 <= racers <= 10 :
            return racers
        else :
            print('Number not in range 2-10. Try again')

def init_turtle_race() :
    screen = turtle.Screen()
    screen.setup(HEIGHT,WIDTH)
    screen.title('Turtle Racing!')

def main() :
    number_of_racers = get_the_number_of_racers()
    racers = [ turtle.Turtle() for i in range(number_of_racers)]
    init_turtle_race()
    get_racers_their_characteristics(racers)
    winner_index = race(racers)
    print(f"The winner is {COLORS[winner_index]} turtle")
    time.sleep(5)
    
main()
