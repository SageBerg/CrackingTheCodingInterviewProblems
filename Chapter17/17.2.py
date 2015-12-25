def has_tic_tac_toe_win(board):
    for row in board:
        if row == ["X", "X", "X"] or row == ["O", "O", "O"]:
            return True
    for col in range(len(board[0])):
        column = []
        for row in range(len(board)):
            column.append(board[row][col])
        if column == ["X", "X", "X"] or column == ["O", "O", "O"]:
            return True
    diagonal = []
    for i in range(len(board)):
        diagonal.append(board[i][i]) 
    if diagonal == ["X", "X", "X"] or diagonal == ["O", "O", "O"]:
        return True
    diagonal = []
    col = len(board[0]) - 1
    row = 0
    while col >= 0:
        diagonal.append(board[row][col])
        col -= 1
        row += 1
    if diagonal == ["X", "X", "X"] or diagonal == ["O", "O", "O"]:
        return True    
    return False


def main():
    board = [ 
                ["O", "X", "O"],  
                ["X", "O", "O"],  
                ["X", "X", "O"]
            ]
    print has_tic_tac_toe_win(board)

main()
