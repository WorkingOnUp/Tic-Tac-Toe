row1 = [' ', ' ', ' ']
row2 = [' ', ' ', ' ']
row3 = [' ', ' ', ' ']
space_count = 0


# function to print the rows of the game board
# Parameters: r1,r2,r3 - the three rows of the board
def display_board(r1, r2, r3):
    print(r1)
    print(r2)
    print(r3)


# function to check if a winning combination has been reached
# Parameter: c - the current player, X or O
def check_win(c):
    return row1[0] == row1[1] == row1[2] == c or row2[0] == row2[1] == row2[2] == c or \
           row3[0] == row3[1] == row3[2] == c or row1[0] == row2[1] == row3[2] == c or \
           row1[2] == row2[1] == row3[0] == c or row1[0] == row2[0] == row3[0] == c or \
           row1[1] == row2[1] == row3[1] == c or row1[2] == row2[2] == row3[2] == c


# function to check if a particular space on the board is full
# Parameter: p - the desired space in range 0 to 9
def is_full(p):
    if p in range(0, 3):
        if row1[p] == ' ':
            return False
        else:
            return True
    elif p in range(3, 6):
        if row2[p - 3] == ' ':
            return False
        else:
            return True
    elif p in range(6, 9):
        if row3[p - 6] == ' ':
            return False
        else:
            return True


# function to place the player's counter at selected space
# Parameters: c - player counter, X or O
#             p - position to place the counter in range 0 to 9
def place_counter(c, p):
    global space_count
    if not is_full(p):
        if p in range(0, 3):
            row1[p] = c
            space_count += 1
            display_board(row1, row2, row3)
        elif p in range(3, 6):
            row2[p - 3] = c
            space_count += 1
            display_board(row1, row2, row3)
        elif p in range(6, 9):
            row3[p - 6] = c
            space_count += 1
            display_board(row1, row2, row3)
    else:
        while is_full(p):
            print('This position is already full! Pick again.')
            p = get_pos()
        place_counter(c, p)
    if check_win(c):
        print("{} is the winner!".format(c))
        space_count = 10


# function to read the current player counter, X or O
def player_counter():
    counter = ''
    while counter not in ['X', 'O']:
        counter = input("Please enter your counter (X or O): ")
        if counter not in ['X', 'O']:
            print('Player can only play as X or O!')
    return counter


# function to read the location on board where counter is to be placed
def get_pos():
    pos = ''
    while pos not in range(0, 10):
        pos = int(input('Enter the grid position where you wish to enter the counter (0-9): '))
        if pos not in range(0, 10):
            print("Please enter a valid position")
    return pos


# function to simulate gameplay
def game():
    cont = 'y'
    while cont == 'y':
        global space_count
        while space_count < 9:
            counter = player_counter()
            pos = get_pos()
            place_counter(counter, pos)
        if space_count == 9:
            print('Board full! There is no winner!')
        cont = input('Do you wish to play again? (Enter y to continue, any other character to exit): ')
        space_count = 0
        row1 = [' ', ' ', ' ']
        row2 = [' ', ' ', ' ']
        row3 = [' ', ' ', ' ']
        display_board(row1, row2, row3)


if __name__ == '__main__':
    display_board(row1, row2, row3)
    game()
