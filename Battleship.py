import random

def find_x2(x1):
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
    return(x2_functions)

def newboard():
    board = []
    #create empty board

    for n in range(0, 25):
        board.append("O ")
    #populate board with "Ocean"

    x1 = random.randint(0, 24)
    #random seed
    
    x2_locations = []
    #empty list of valid x2 locations

    x2_functions = find_x2(x1)
    #calls function
    
    for m in x2_functions:
        x2 = m(x1)
        if x2 <= 24 and x2 >=0:
            x2_locations.append(x2)
    #determines valid x2 locations and appends them to x2_locations

    board[x1] = "S "
    x2 = random.choice(x2_locations)
    board[x2] = "S "
    return(board)

def newgame(r):
    print '\n'.join(''.join(r[i:i+5]) for i in xrange(0,25,5))
    print('---------')
    #prints board

    positions =  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
    tried_positions = []
    #possible places to attack

    moves = 0
    #initial moves value
    
    while True:
        available_positions = []
        for element in positions:
            if element not in tried_positions:
                available_positions.append(element)
        index = random.choice(available_positions)
        if r[index] == "O ":
            moves = moves + 1
            tried_positions.append(index)
            r[index] = "M "
        else:
            moves = moves + 1
            r[index] = "X "
            hit = index
            break
    #loops, randomly choosing moves until a ship is found

    x2_functions = find_x2(hit)
    #calls function

    sink_positions = []
    for m in x2_functions:
        x2 = m(hit)
        if x2 <= 24 and x2 >=0:
            if x2 not in tried_positions:
                sink_positions.append(x2)
    #determines valid x2 locations and appends them to x2_locations

    while True:
        available_positions = []
        for element in sink_positions:
            if element not in tried_positions:
                available_positions.append(element)
        index = random.choice(available_positions)
        if r[index] == "O ":
            moves = moves + 1
            tried_positions.append(index)
            r[index] = "M "
        else:
            moves = moves + 1
            r[index] = "X "
            hit = index
            break
    #loops, randomly choosing moves until the ship is destroyed
            
    print '\n'.join(''.join(r[i:i+5]) for i in xrange(0,25,5))
    print("Game over!")
    print("It took %d moves to sink the ship" %moves)
    #prints out the final board
    
round_board = newboard()    
newgame(round_board)
