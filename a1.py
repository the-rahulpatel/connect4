# DO NOT modify or add any import statements
from typing import Optional
from a1_support import *

# Name:Rahul Patel
# Student Number:48043090
# ----------------

# Write your classes and functions here

def num_hours() -> float:
    return 30.0

def generate_initial_board() -> list[str]:
    """Returns an empty board with empty strings.

    Return:
        list[str]: An empty 8x8 board. 

    >>> generate_initial_board()
    ['--------','--------','--------','--------','--------',
    '--------','--------','--------']
    """
    board = []
    for _ in range(BOARD_SIZE):
        board.append(BOARD_SIZE*BLANK_PIECE) 
    return board


def is_column_full(column:str) -> bool:
    """Returns True if and only if the column contains a hyphen. 
       
    Parameters:
        column(str): 8-character long string, each character is a row.

    Returns:
        bool: True if 'column' doesn't contain any hyphen,
              False otherwise.
         
    >>> column = "---XOXXX"
    >>> is_column_full(column)
    False
    """
    
    count = 0 
    for i in column:
        if i == BLANK_PIECE:
            count = count + 1
            
    #if any hyphen exists, then false, otherwise True. 
    return False if count else True


def is_column_empty(column:str) -> bool:
    """Returns True iff every character in 'column' is a hyphen.

    Parameters:
        column (str): an 8-character long string and each character
                      is a row. 

    Returns:
        bool: True iff every character in 'column' is a hyphen, false
              otherwise
        
    >>> column = "--------"
    >>> is_column_empty(column)
    True
    """
    
    count = 0
    for i in column:
        if i == BLANK_PIECE:
            count = count + 1
    #if the entire column is filled with hyphens, then True
    #Otherwise, false. 
    return True if count == len(column) else False


def rows_to_columns(board:list[str]) -> list[str]:
    """Returns 'board' with its columns transformed into rows.

    Parameters:
        board (list[str]): A list with 8 columns and
                           each column has rows.

    Returns:
        list[str]: A list with 8 rows and each row has columns.
        
    >>> board = ['--------', '----OOOO', 'XXXXXXXX', '--------',
    '------XO','--------', '---XXOXO', '--------']
    >>> rows_to_columns(board)
    ['--X-----', '--X-----', '--X-----', '--X---X-', '-OX---X-',
    '-OX---O-','-OX-X-X-', '-OX-O-O-']
    """
    rows = []
    for i in range(BOARD_SIZE):
        #empty strings to create a column each iteration.
        each_row = ''
        for column in board:
            each_row += column[i]
        rows.append(each_row)
    return rows


def display_board(board:list[str]) -> None:
    """Prints 'board' with the appropriate layout and
    a horizontal number below. 

    Parameters:
        board (list[str]): A list with 8 columns and each column
                           has rows.

    Preconditions:
        board (list[str]): A list with 8 columns and each
                           with 8 characters.
          
    >>> board = generate_initial_board()
    >>> display_board(board)
    |-|-|-|-|-|-|-|-|
    |-|-|-|-|-|-|-|-|
    |-|-|-|-|-|-|-|-|
    |-|-|-|-|-|-|-|-|
    |-|-|-|-|-|-|-|-|
    |-|-|-|-|-|-|-|-|
    |-|-|-|-|-|-|-|-|
    |-|-|-|-|-|-|-|-|
     1 2 3 4 5 6 7 8
    """
    horizontal_number = ''
    for number in range(1,BOARD_SIZE+1):
        #We add numbers side by side
        horizontal_number = horizontal_number + str(number)
        
    space = ' '
    #we convert rows in board to columns for an easier presentation
    rows = rows_to_columns(board)
    for row in rows:
        print(COLUMN_SEPARATOR + COLUMN_SEPARATOR.join(row) +
              COLUMN_SEPARATOR)
    print(space + space.join(horizontal_number) + space)
    return None


def check_input(command:str) -> bool:
    """Returns True iff 'command' is valid, false otherwise.  
    
    Parameters:
        command (str): a column with 8 rows.

    Returns:
        bool: True when 'command' is valid, false when it is invalid. 
    
    >>> command = 'a7'
    >>> check_input(command)
    True
    >>> command = '1a'
    >>> check_input(command)
    Invalid command. Enter 'h' for valid command format
    False    
    """
    
    if len(command) == 2:
        #we use the lower() to discard any uppercase clashes
        #the .isidigit() ensures the digit represents a column
        if (command[0].lower() in ['a','r']
            and command[1].isdigit()):
            #we ensure the given action has appropriate column
            if int(command[1])-1 in range(BOARD_SIZE):
                return True
            print(INVALID_COLUMN_MESSAGE)
            return False
        else:
            print(INVALID_FORMAT_MESSAGE)
            return False
    elif len(command) == 1:
        #we make sure the only single letter is help or quit. 
        if command.lower() in ['h','q']:
            return True
        print(INVALID_FORMAT_MESSAGE)
        return False
    print(INVALID_FORMAT_MESSAGE)
    return False


def get_action() -> str:
    """Prompts a user to enter until the command is valid, otherwise
    relevant messages are displayed. 

    Returns:
        str: 'command' that is valid and corresponds to an action. 

    >>> get_action()
    Please enter action (h to see valid commands): a-1
    Invalid command. Enter 'h' for valid command format
    Please enter action (h to see valid commands): r
    Invalid command. Enter 'h' for valid command format
    Please enter action (h to see valid commands): r4
    'r4'
    >>> get_action()
    Please enter action (h to see valid commands): g
    Invalid command. Enter 'h' for valid command format
    Please enter action (h to see valid commands): help
    Invalid command. Enter 'h' for valid command format
    Please enter action (h to see valid commands): H
    'H'
    """
    end = False
    command = ''


    while not end:
        user_input = input(ENTER_COMMAND_MESSAGE)
        if check_input(user_input):
            command = user_input
            break
    return command

def add_piece(board: list[str], piece:str,column_index:int) -> bool:
    """Returns True when 'column_index' in 'board'
    correspondsto a column that is not full and 'piece' is placed,
    otherwise returns false.

    Parameters:
        board (list[str]): A sequence of columns and each column
                           has rows.
        piece (str): one-character string, either a cross
                     or a naught.
        column_index (int): the index of a column that is between
                            0 and 7 inclusive.

    Returns:
        bool: True iff the corresponding 'column_index' is
              referring to an incomplete column, otherwise false. 
        
    >>> board = ['--------', '----OOOO', 'XXXXXXXX', '--------',
    '------XO','--------', '---XXOXO', '--------']
    >>> add_piece(board, "X", 1)
    True
    >>> board
    ['--------', '---XOOOO', 'XXXXXXXX', '--------', '------XO',
    '--------','---XXOXO', '--------']
    >>> add_piece(board, "O", 2)
    You can't add a piece to a full column!
    False
    """
    column = board[column_index]
    rows = list(column)
    if is_column_full(column):
        print(FULL_COLUMN_MESSAGE)
        return False
    # find the index of the first empty from the bottom. 
    index = column.rfind('-')
    rows[index] = piece
    column = ''.join(rows)
    # update the previous board with new modifications
    board[column_index] = column
    return True


def remove_duplicates(old_list: list) -> list:
    """Returns a list without duplicates from the original list.

    Parameters:
        old_list (list): A list with possible duplicate.

    Returns:
        list: A list with no duplicates. 

    >>> winners_list = ["X","O","X"]
    >>> distinct_list = remove_duplicates(winners_list)
    >>> distinct_list
    ["O","X"]
    """
    distinct_list = []
    for i in old_list:
        if i not in distinct_list: # we ensure it doesn't exist already
            distinct_list.append(i)
    return distinct_list


def remove_piece(board: list[str],column_index:int) -> bool:
    """Returns false when the column is empty, otherwise a piece is
    removed from the board and it returns True.

    >>> board = ['--------', '----OOOO', 'XXOOOXXX', '--------',
    '------XO','--------', '---XXOXO', '--------']
    >>> remove_piece(board,2)
    True
    >>> board
    ['--------', '----OOOO', '-XXOOOXX', '--------', '------XO',
    '--------','---XXOXO', '--------']
    >>> remove_piece(board,0)
    You can't remove a piece from an empty column!
    False
    """
    
    column = board[column_index]
    if is_column_empty(column):
        print(EMPTY_COLUMN_MESSAGE)
        return False
    column = list(column)
    column.pop()
    column.insert(0,'-')
    column = ''.join(column)
    board[column_index] = column
    return True


def declare_decision(given_list:list) -> Optional[str]:
    """Returns None if the string is empty,
    otherwise a string is returned.

    Parameters:
        given_list (list): A list with one, many or no winners.

    Returns: 
        None: None if no winnner and 'give_list' is empty.
        str: String when it's either one or many winners. 

    >>> winners_list = ["O", "X"]
    >>> final_answer = declare_decision(winners_list)
    >>> final_answer
    '-'
    >>> winners_list = ["X"]
    >>> final_answer = declare_decision(winners_list)
    >>> final_answer
    'X'
    """
    if len(given_list) > 1: # checks if there are multiple winners
        return '-' # declare draw in that case
    elif len(given_list) == 1:
        return given_list[0]
    return None # neither a draw nor any winner


def check_vertical(board:list[str]) -> Optional[str]:
    """Returns None when a winner is not find vertically,
    otherwise the result is returned. 
    
    Parameters:
        board (list[str]): A list with 8 columns and each column
                           has rows.

    Returns:
        none: None if no piece is found with the winning sequence.
        str: A string with either the winning piece or a hyphen to
             symbolise draw.
        
    >>> board = ['---XXXXO', '-------O', '-------O', '-------O',
    '--------','--------', '--------', '--------']
    >>> check_vertical(board)
    'X'   
    """
    
    winners = []
    for column in board:
        #checks if the sequence of winning moves exists
        if REQUIRED_WIN_LENGTH*PLAYER_1_PIECE in column:
            #we add the appropriate player to the winning list. 
            winners.append(PLAYER_1_PIECE)
        elif REQUIRED_WIN_LENGTH*PLAYER_2_PIECE in column:
            winners.append(PLAYER_2_PIECE)

    #discarding any repeating winners and declaring the result
    #from unique outputs
    distincts = remove_duplicates(winners)
    final_output = declare_decision(distincts)
    return final_output


def check_horizontal(board:list[str]) -> Optional[str]:
    """Returns None when a winner is not found horizontally, otherwise
    the result is returned.

    Parameters:
        board (list[str]): A list with 8 columns and each column
                           has rows.

    Returns:
        none: None if no piece is found with the winning sequence.
        str: A string with either the winning piece or a hyphen to
             symbolise draw.
    """
    #transforms horizontals into vertical and utilises
    #the check_vertical to deduce the outcome
    rows = rows_to_columns(board)
    return check_vertical(rows)


def check_diagonal(board:list[str]) -> Optional[str]:
    """Returns None when a winner is not found diagonally, otherwise
    the result is returned.

    Parameters:
        board (list[str]): A list with 8 columns and each column
                           has rows.

    Returns:
        none: None if no piece is found with the winning sequence.
        str: A string with either the winning piece or a hyphen to
             symbolise draw.
    """

    
    pieces = [PLAYER_1_PIECE, PLAYER_2_PIECE]
    winners = []
    
    for piece in pieces:

        
        # checks diagonals in the positive gradient direction
        # or right-up.

        # sets upper bound for columns to half the board size (inclusive),
        for column in range((BOARD_SIZE//2)+1):
            # ensures the first row must have 4 sequences consecutively
            # in the right-up direction. 
            for row in range((BOARD_SIZE//2)-1,BOARD_SIZE):
                # checks if each 4 pairs of (column,row) leads to
                # the same piece as gradient increases
                if (board[column][row] == piece
                    and board[column + 1][row - 1] == piece
                    and board[column + 2][row - 2] == piece
                    and board[column + 3][row - 3] == piece):
                    winners.append(piece)

        # checks diagonals in the negative gradient direction
        # or right-down.
        for column in range((BOARD_SIZE//2)+1):
            # inspects the first right-down sequence begins from the
            # origin up up to the next 4 consecutively (inclusive). 
            for row in range((BOARD_SIZE//2)+1):
                # if the winning sequences as gradient decreases is
                # found then the matching piece is added to the
                # winners list. 
                if (board[column][row] == piece
                    and board[column + 1][row + 1] == piece
                    and board[column + 2][row + 2] == piece
                    and board[column + 3][row + 3] == piece):
                    winners.append(piece)

    distincts = remove_duplicates(winners)
    final_output = declare_decision(distincts)
    return final_output

def check_win(board:list[str]) -> Optional[str]:
    """Returns None when no result is declared, otherwise the outcome
    is returned.

    Parameters:
        board (list[str]): A list with 8 columns and each column
                           has rows.

    Returns:
        None: None when no broken lines are formed. 
        str: a result if one or two unbroken lines are formed. 
        
    """
    
    horizontal = check_horizontal(board) 
    vertical = check_vertical(board)
    diagonal = check_diagonal(board)
    combined_list = [horizontal, vertical, diagonal]
    winners = []

    for i in combined_list:
        if i not in winners and i != None: # ensures a must result
            winners.append(i)
    final_answer = declare_decision(winners)
    return final_answer

def play_game() -> None:
    """Utilizes the necessary functions to coordinate a single game
    from beginning to end.
    """
    
    board = generate_initial_board()
    turns = [PLAYER_1_PIECE,PLAYER_2_PIECE]

    turn_decider = 0 #Validates that PlayerX's turn must come first
    player = None
    outcome = None
    user_quits = False
    
    while True:
        display_board(board)
        turn_decider = turn_decider % 2 #PlayerX's turn comes first
        piece = turns[turn_decider] # retrieves the piece of the player
        not_passed = True
        print(f"Player {turn_decider+1} to move")

        # makes sure the user must enter a valid command to move 
        # forward with the game.
        
        while not_passed:
            move = get_action()
            if len(move) != 1:   
                column = int(move[1])-1
                if move[0] == 'a':
                    if not is_column_full(board[column]):
                        add_piece(board,piece,column)
                        # breaks the loop as valid input is entered.
                        not_passed = False
                    else:
                        print(FULL_COLUMN_MESSAGE)
                else:
                    if not is_column_empty(board[column]):
                        remove_piece(board,column)
                        not_passed = False
                    else:
                        print(EMPTY_COLUMN_MESSAGE)
            else:
                if move.lower() == 'h':
                    print(HELP_MESSAGE)
                    display_board(board)
                    # increments to display appropriate player number.
                    print(f"Player {turn_decider+1} to move")
                    
                else:
                    not_passed = False #breaks when user quits

        # stops the game and we save the reason so, we can distinguish
        # this from a completion of game. 
        if move.lower() == 'q':
            user_quits = True
            break

        result = check_win(board)
        if result:
            outcome = result
            break
        turn_decider += 1

    
    # if a game is completed, and either draw or the winning
    # is deduced and displayed.
    if not user_quits:
        display_board(board)
        if outcome in turns:
            if outcome == 'X':
                print(PLAYER_1_VICTORY_MESSAGE)
            else:
                print(PLAYER_2_VICTORY_MESSAGE)
        else:
            print(DRAW_MESSAGE)
    return None

def main() -> None:
    """Enacts a full game with a prompt to restart.
    """
    while True:
        play_game()
        repeat_input = input(CONTINUE_MESSAGE)
        if repeat_input.lower() != 'y':
            break
    return None

if __name__ == "__main__":
    main()                                                                         
