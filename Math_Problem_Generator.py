import random
import time

OPERATORS = ["+", "-", "*"]
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROBLEMS = 10

def generate_problem() :
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS) #chooses randomly an element from the list

    expr = str(left) + " " + operator + " " + str(right)
    ans = eval(expr) #this function evaulates a string expression as if it were python code
    return expr, ans

wrong = 0

input("Press enter to start")
print("---------------------------------")

start_time = time.time()

for i in range(TOTAL_PROBLEMS) :
    expr, ans = generate_problem()
    while True : 
        guess = input("Problem #" + str(i+1) + ": " + expr + "= ")
        if(str(ans) == guess) : # dont convert guess to int as if guess is not a valid integer, it would crash the program
            break

end_time = time.time()
total_time = end_time - start_time

print("-----------------------------------")
print("Nice Work! You finished in", round(total_time, 2),"seconds.")
print("Your accuracy is", round(10 *100/(wrong+10), 2))