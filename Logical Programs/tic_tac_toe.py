import random

def initialize_board():
    """Initialize a 3x3 Tic-Tac-Toe board with empty spaces.
    
    Returns:
        list: A 3x3 list of lists filled with spaces (" ")
    """
    return [[" " for _ in range(3)] for _ in range(3)]

def print_board(board):
    """Print the current state of the Tic-Tac-Toe board.
    
    Arguments:
        board (list): A 3x3 list representing the game board
    """
    for row in board:
        print("|".join(row))
        print("-" * 5)

def is_valid_move(board, row, col):
    """Check if a move is valid (within bounds and cell is empty).
    
    Arguments:
        board (list): A 3x3 list representing the game board
        row (int): Row index (0-2)
        col (int): Column index (0-2)
    
    Returns:
        bool: True if move is valid, False otherwise
    """
    return 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " "

def check_winner(board, player):
    """Check if the specified player has won the game.
    
    Arguments:
        board (list): A 3x3 list representing the game board
        player (str): The player's symbol ("X" or "O")
    
    Returns:
        bool: True if player has won, False otherwise
    """
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True
    
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    
    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    
    return False

def is_board_full(board):
    """Check if the board is completely filled (no empty spaces).
    
    Arguments:
        board (list): A 3x3 list representing the game board
    
    Returns:
        bool: True if board is full, False otherwise
    """
    return all(cell != " " for row in board for cell in row)

def computer_move(board):
    """Generate a random move for the computer.
    
    Arguments:
        board (list): A 3x3 list representing the game board
    
    Returns:
        tuple: (row, col) coordinates of the computer's move
    """
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if is_valid_move(board, row, col):
            return row, col

def play_game():
    """Run the Tic-Tac-Toe game between player (X) and computer (O).
    
    Manages the game loop, alternates turns, and determines the winner or draw.
    """
    board = initialize_board()
    print("Welcome to Tic-Tac-Toe!")
    print("Enter row (0-2) and column (0-2) separated by space")

    while True:
        # Computer's turn
        row, col = computer_move(board)
        board[row][col] = "O"
        print(f"\nComputer chooses: Row {row}, Col {col}")
        print_board(board)

        if check_winner(board, "O"):
            print("Computer wins!")
            break
        if is_board_full(board):
            print("It's a draw!")
            break

        # Player's turn
        while True:
            try:
                row, col = map(int, input("Your turn (row col): ").split())
                if is_valid_move(board, row, col):
                    break
                print("Invalid move! Cell is occupied or out of range. Try again.")
            except ValueError:
                print("Invalid input! Enter two numbers (0-2) separated by space.")

        board[row][col] = "X"
        print(f"\nYou chose: Row {row}, Col {col}")
        print_board(board)

        if check_winner(board, "X"):
            print("You win!")
            break
        if is_board_full(board):
            print("It's a draw!")
            break

# Start the game
play_game()