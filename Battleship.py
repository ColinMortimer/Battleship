import random

def newboard():
    board = []
    #create empty board

    for n in range(0, 25):
        board.append("O ")
    #populate board with "Ocean"

    x1 = random.randint(0, 24)
    #random seed
    
    def m1(x1):
        x2 = x1-1
        return(x2)
    def m2(x1):
        x2 = x1+1
        return(x2)
    def m3(x1):
        x2 = x1-5
        return(x2)
    def m4(x1):
        x2 = x1+5
        return(x2)
    #possible ship directions

    left_c = [5, 10, 15, 20]
    right_c = [4, 9, 14, 19]
    #defines fringe cases

    if x1 in left_c:
        x2_functions = [m2, m3, m4]
    elif x1 in right_c:
        x2_functions = [m1, m3, m4]
    else:
        x2_functions = [m1, m2, m3, m4]
        
    #possible x2 functions based in x1's location
    
    x2_locations = []
    #empty list of valid x2 locations
    
    for m in x2_functions:
        x2 = m(x1)
        if x2 <= 24 and x2 >=0:
            x2_locations.append(x2)
    #determines valid x2 locations and appends them to x2_locations

    board[x1] = "S "
    x2 = random.choice(x2_locations)
    board[x2] = "S "
    return(board)

round_board = newboard()
#define round's board

def newgame(r):
    print '\n'.join(''.join(r[i:i+5]) for i in xrange(0,25,5))
    #prints board

    positions =  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
    tried_positions = []
    #possible places to attack

    moves = 1

    while True:
        available_positions = []
        for element in positions:
            if element not in tried_positions:
                available_positions.append(element)
        index = random.choice(available_positions)
        if r[index] == "O ":
            moves = moves + 1
            tried_positions.append(index)
        else:
            break
        
    print(moves)
    
newgame(round_board)
