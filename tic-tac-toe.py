answer = ""
turn = 1

table = [
    ["1","|","2","|","3"],
    ["-","+","-","+","-"],
    ["4","|","5","|","6"],
    ["-","+","-","+","-"],
    ["7","|","8","|","9"],
]

def main():
    play = ""
    player = True
    winner = False
    symbol = ""
    print_table(table)
    while winner == False and turn <= 9:
            if player:
                symbol = "x"
                play = input("x's turn to choose a square (1-9): ")
            else:
                symbol = "o"
                play = input("o's turn to choose a square (1-9): ")
            change = make_changes(table,turn,play,symbol)
            if change == 1:
                print_table(table)
                if player:
                    player = False
                else:
                    player = True
                winner = get_winner(table)
    if winner:
        if symbol == "x":
            print("Player number 1 wins!")
        else: 
            print("Player number 2 wins!")
    else:
        print_table("the match ended tied")

def get_winner(table):
    
    row0 = table[0][0] == table[0][2] == table[0][4]
    row2 = table[2][0] == table[2][2] == table[2][4]
    row4 = table[4][0] == table[4][2] == table[4][4]
    column0 = table[0][0] == table[2][0] == table[4][0]
    column2 = table[0][2] == table[2][2] == table[4][2]
    column4 = table[0][4] == table[2][4] == table[4][4]
    diagonal1 = table[0][0] == table[2][2] == table[4][4]
    diagonal2 = table[0][4] == table[2][2] == table[4][0]
    if row0 or row2 or row4 or column0 or column2 or column4 or diagonal1 or diagonal2:
        return True
    else:
        return False

def print_table(table):
    for fila in table:
        for i in range(len(fila)):
            if i == len(fila) - 1:
                print(fila[i], end='\n')
            else:
                print(fila[i], end='  ')

def make_changes(table,turn,play,symbol):
    busy = "That place is a busy. Please, type another number!"
    error_number = "That number is incorrect. Please, type another number"
        
    if play == "1": 
        if table[0][0] == "1":
            table[0][0] = symbol
            turn += 1
            return 1
        elif table[0][0] == "x" or table[0][0] == "y":
            print(busy)
    elif play == "2": 
        if table[0][2] == "2":
            table[0][2] = symbol
            turn += 1
            return 1
        elif table[0][2] == "x" or table[0][2] == "y":
            print(busy)
            
    elif play == "3": 
        if table[0][4] == "3":
            table[0][4] = symbol
            turn += 1
            return 1
        elif table[0][4] == "x" or table[0][4] == "y":
            print(busy)
            
    elif play == "4": 
        if table[2][0] == "4":
            table[2][0] = symbol
            turn += 1
            return 1
        elif table[2][0] == "x" or table[2][0] == "y":
            print(busy)
            
    elif play == "5": 
        if table[2][2] == "5":
            table[2][2] = symbol
            turn += 1
            return 1
        elif table[2][2] == "x" or table[2][2] == "y":
            print(busy)
            
    elif play == "6":
        if table[2][4] == "6":
            table[2][4] = symbol
            turn += 1
            return 1
        elif table[2][4] == "x" or table[2][4] == "y":
            print(busy)
            
    elif play == "7": 
        if table[4][0] == "7":
            table[4][0] = symbol
            turn += 1
            return 1
        elif table[4][0] == "x" or table[4][0] == "y":
            print(busy)
            
    elif play == "8": 
        if table[4][2] == "8":
            table[4][2] = symbol
            turn += 1
            return 1
        elif table[4][2] == "x" or table[4][2] == "y":
            print(busy)
            
    elif play == "9": 
        if table[4][4] == "9":
            table[4][4] = symbol
            turn += 1
            return 1
        elif table[4][4] == "x" or table[4][4] == "y":
            print(busy)
    else:
        print(error_number)

if __name__ == "__main__":
    main()
