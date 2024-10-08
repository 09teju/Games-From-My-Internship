def create_board():
    return [[' ' for _ in range(7)] for _ in range(6)]

def print_board(board):
    for row in board:
        print('|'.join(row))
        print('-' * 13)

def drop_piece(board, column, piece):
    for row in reversed(board):
        if row[column] == ' ':
            row[column] = piece
            return True
    return False

def is_winning_move(board, piece):
    # Check horizontal, vertical, and diagonal locations for a win
    for c in range(7):
        for r in range(6):
            if (c + 3 < 7 and 
                board[r][c] == piece and 
                board[r][c + 1] == piece and 
                board[r][c + 2] == piece and 
                board[r][c + 3] == piece):
                return True

            if (r + 3 < 6):
                if (board[r][c] == piece and 
                    board[r + 1][c] == piece and 
                    board[r + 2][c] == piece and 
                    board[r + 3][c] == piece):
                    return True

                if (c + 3 < 7 and 
                    board[r][c] == piece and 
                    board[r + 1][c + 1] == piece and 
                    board[r + 2][c + 2] == piece and 
                    board[r + 3][c + 3] == piece):
                    return True

                if (c - 3 >= 0 and 
                    board[r][c] == piece and 
                    board[r + 1][c - 1] == piece and 
                    board[r + 2][c - 2] == piece and 
                    board[r + 3][c - 3] == piece):
                    return True

def main():
    board = create_board()
    game_over = False
    turn = 0

    print("Welcome to Connect 4!")
    print_board(board)

    while not game_over:
        column = int(input(f"Player {turn % 2 + 1}, choose a column (0-6): "))

        if 0 <= column < 7 and drop_piece(board, column, 'X' if turn % 2 == 0 else 'O'):
            print_board(board)

            if is_winning_move(board, 'X' if turn % 2 == 0 else 'O'):
                print(f"Player {turn % 2 + 1} wins!")
                game_over = True

            turn += 1
        else:
            print("Invalid move. Try again.")

if __name__ == "__main__":
    main()
