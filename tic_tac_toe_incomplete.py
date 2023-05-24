from random import randrange
b =[[1, 2, 3], [4, "X", 6], [7, 8, 9]]
game = True




def display_board(b):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    print(f"""
+-------+-------+-------+
|       |       |       |
|   {b[0][0]}   |   {b[0][1]}   |   {b[0][2]}   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   {b[1][0]}   |   {b[1][1]}   |   {b[1][2]}   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   {b[2][0]}   |   {b[2][1]}   |   {b[2][2]}   |
|       |       |       |
+-------+-------+-------+""")

def enter_move(b):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    spaces = make_list_of_free_fields(b)
    avalible = spaces
    player_turn = True
    
    while player_turn:
        move = int(input("Choose a space: ")) -1
        #creating the tuple
        move_tuple =(move//3,move%3)
        if move_tuple in spaces:
            (row,col) = move_tuple
            b[row][col] = "O"
            # avalible.remove(move_tuple)
            # print(avalible)
            # if avalible == []:
            #     return False
            
        
            
            player_turn = False
        

def make_list_of_free_fields(b):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    free = []
    avalible = free

    for i in range(len(b)):
        for j in range(len(b[i])):
            if b[i][j] in [1, 2, 3, 4, 5, 6 ,7 ,8 ,9]:
                if b[i][j] != 'O' or 'X':
                    free.append((i, j))

    return free
    
def victory_for(b, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    global game
    player = 'Player wins!'
    computer = 'Computer wins!'
    draw = "Draw!"
    spaces = make_list_of_free_fields(b)
    pwin = False
    cwin = False
    if cwin == True or  pwin == True:
        game = False
    
    
    if pwin== True:
        cwin == False
    #Across
    if b[0][0] == b[0][1] == b[0][2] == sign:
        if sign == 'X':
            if pwin == False:
                print(computer)
                game = False
                cwin = True
        elif sign == 'O':
            print(player)
            game = False
            pwin = True
    

    if b[1][0] == b[1][1] == b[1][2] == sign:
        if sign == 'X':
            if pwin == False:
                cwin = True
                print(computer)
                game = False        
        elif sign == 'O':
            print(player)
            game = False
            

    if b[2][0] == b[2][1] == b[2][2] == sign:
        if sign == 'X':
            if pwin == False:
                cwin = True
                print(computer)
                game = False     
        elif sign == 'O':
            print(player)
            game = False
            pwin = True

    #horizontal
    if b[0][0] == b[1][0] == b[2][0] == sign:
        if sign == 'X':
            if pwin == False:
                print(computer)
                game = False
                
                cwin = True
        elif sign == 'O':
            print(player)
            game = False
            pwin = True 
    if b[0][1] == b[1][1] == b[2][1] == sign:
        if sign == 'X':
                if pwin == False:
                    print(computer)
                    game = False
                    cwin = True
        elif sign == 'O':
            print(player)
            game = False
            pwin = True  
    if b[0][2] == b[1][2] == b[2][2] == sign:
        if sign == 'X':
            if pwin == False:
                cwin = True
                print(computer)
                game = False
        elif sign == 'O':
            print(player)
            game = False
            pwin = True 
    #diag
    if b[0][0] == b[1][1] == b[2][2] == sign:
        if sign == 'X':
            if pwin == False:
                cwin = True
                print(computer)
                game = False
        elif sign == 'O':
            print(player)
            game = False
            pwin = True
    if b[0][2] == b[1][1] == b[2][0] == sign:
        if sign == 'X':
            if pwin == False:
                cwin = True
                print(computer)
                game = False
        elif sign == 'O':
            print(player)
            game = False 
            pwin = True
            
    if spaces == []:
        if cwin == False and pwin == False:
            print(draw)
            game = False
  




 




    
        

        
        
        
    
    


   

def draw_move(b):
     # The function draws the computer's move and updates the board.
     # I belive i need to finish the function make_list_of_free_fields(b)
     #Before i can do this function.
    spaces = make_list_of_free_fields(b)
    comp_turn = True
    avalible = spaces
    
    while comp_turn:
        computer = randrange(0, 9)
        comp_tuple =(computer//3,computer%3)
        if comp_tuple in spaces:
            (row,col) = comp_tuple
            b[row][col] = "X"
            comp_turn = False





     
    
         
while game:
    display_board(b)
    make_list_of_free_fields(b) 
    enter_move(b)
    victory_for(b, sign='O')
    draw_move(b)
    victory_for(b, 'X')
display_board(b)


