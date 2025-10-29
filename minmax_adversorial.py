import math

# Initialize board
board = [" " for _ in range(9)]

# Display the board
def print_board():
    print()
    for i in range(3):
        print(" | ".join(board[i*3:(i+1)*3]))
        if i < 2:
            print("-" * 9)
    print()

# Check for a winner
def winner(b):
    # All winning combinations
    win_combos = [(0,1,2), (3,4,5), (6,7,8),  # rows
                  (0,3,6), (1,4,7), (2,5,8),  # cols
                  (0,4,8), (2,4,6)]            # diagonals
    for (x,y,z) in win_combos:
        if b[x] == b[y] == b[z] and b[x] != " ":
            return b[x]
    return None

# Check if the board is full
def is_full(b):
    return " " not in b

# Minimax algorithm
def minimax(b, depth, is_maximizing):
    win = winner(b)
    if win == "O":
        return 1
    elif win == "X":
        return -1
    elif is_full(b):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if b[i] == " ":
                b[i] = "O"
                score = minimax(b, depth + 1, False)
                b[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if b[i] == " ":
                b[i] = "X"
                score = minimax(b, depth + 1, True)
                b[i] = " "
                best_score = min(score, best_score)
        return best_score

# AI move
def ai_move():
    best_score = -math.inf
    move = None
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, 0, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    board[move] = "O"

# Main game loop
def play():
    print("Welcome to Tic Tac Toe! (You are X, AI is O)")
    print_board()

    while True:
        # Human move
        move = int(input("Enter your move (1-9): ")) - 1
        if board[move] != " ":
            print("Invalid move. Try again.")
            continue
        board[move] = "X"

        print_board()
        if winner(board) == "X":
            print("You win! ")
            break
        elif is_full(board):
            print("It's a tie!")
            break

        # AI move
        print("AI is thinking...")
        ai_move()
        print_board()

        if winner(board) == "O":
            print("AI wins! ")
            break
        elif is_full(board):
            print("It's a tie!")
            break

# Run the game
play()
