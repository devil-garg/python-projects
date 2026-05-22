import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A" : "2",
    "B" : "3",
    "C" : "5",
    "D" : "6"
}

symbol_values = {
    "A" : 5,
    "B" : 2,
    "C" : 7,
    "D" : 4
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_in_lines = [ 0 for i in range(lines)]
    for row in range(lines) :
        symbol = columns[0][row]
        for column in columns :
            symbol_to_check = column[row]
            if symbol != symbol_to_check :
                break
        else :
            winning_in_lines[row] = values[symbol] * bet
            winnings += winning_in_lines[row]      
    
    return winning_in_lines,winnings

def get_slot_machine_spin(rows, cols, symbols) :
    all_symbols = []
    for symbol,count in symbols.items() :
        for _ in range(int(count)) :
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols) :
        column = []
        current_symbols = all_symbols
        for _ in range(rows) :
            value = random.choice(current_symbols)
            column.append(value)
            all_symbols.remove(value)
        columns.append(column) #we have columns appended as rows here

    return columns

def print_slot_machine(columns) :
    for row in range(len(columns[0])) :
        for i, column in enumerate(columns) :
            if i != len(columns) - 1 :
                print(column[row] ,end="|") #end= default value is new line but we can set it ourselves
            else :
                print(column[row], end="")
        
        print()

def deposit() :
    while True : 
        amount = input("What would you like to deposit? $")
        if amount.isdigit() :
            amount = int(amount)
            if amount > 0 :
                break
            else :
                print("Enter a valid amount > 0")
        else : 
            print("Enter a valid amount!")

    return amount

def get_number_of_lines() :
    while True : 
        lines = input("Enter the number of lines you want to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit() :
            lines = int(lines)
            if 0 < lines <= MAX_LINES :
                break
            else :
                print("Enter a valid number of lines(1-" + str(MAX_LINES) + ")")
        else : 
            print("Enter a valid NUMBER!")

    return lines

def get_bet() :
    while True : 
        amount = input("What would you like to bet? $")
        if amount.isdigit() :
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET :
                break
            else :
                print(f"Enter a valid amount between ${MIN_BET} - ${MAX_BET}")
        else : 
            print("Enter a valid amount!")

    return amount

def spin(balance) :
    lines = get_number_of_lines()

    while True :
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance :
            print(f"Insufficient balance! Your total bet exceeds your balance")
            choice = input("Do you want to deposit more? (y or n)").lower()
            if choice == 'y' :
                balance += deposit()
            elif choice == 'n' :
                print(f"Choose a bet that totals less than your current balance: {balance}")
            else :
                print("Provide a valid input")
        else :
            break

    print(f"You are betting ${bet} each on {lines} lines. Your total bet is ${total_bet}")

    slots = get_slot_machine_spin(ROWS,COLS,symbol_count)
    print_slot_machine(slots)

    winning_in_lines,winnings = check_winnings(slots,lines,bet,symbol_values)
    print(f"You have won {winning_in_lines} in corresponding lines")
    print("Total Winnings:",winnings)

    return winnings+balance-total_bet

def main() :
    balance = deposit()
    balance = spin(balance)
    while True : 
        print("Your Current Balance:", balance)
        choice = input("Do you want to quit or play more? (q)(p) ").lower()
        if choice == 'q' :
            print("Bye! Have a nice day!")
            exit()
        elif choice == "p" :
            balance = spin(balance)

main()