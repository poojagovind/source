Suppose that two players are playing a tic-tac-toe game on an × n×n board. They’re following specific rules to play and win the game.
A move is guaranteed to be valid if a mark is placed on an empty block.
No more moves are allowed once a winning condition is reached.
A player who succeeds in placing n of their marks in a horizontal, vertical, or diagonal row wins the game.
Your task is to implement a TicTacToe class, which will be used by two players to play the game and win fairly.

Keep in mind the following functionalities that need to be implemented:

The TicTacToe class, which declares an object to create the board.
Init (n), which initializes the object of TicTacToe to create the board of size n.
Move (row, col, player) indicates that the player with ID player plays at the board’s cell (row,col). The move is guaranteed to be a valid move. At each move, this function returns the player ID if any player wins and returns 0 if no one wins.

class TicTacToe:
    # TicTacToe class contains rows, cols, diagonal,
    # and anti_diagonal to create a board.
    # Constructor is used to create n * n tic - tac - toe board.
    def __init__(self, n):
        self.rows = [0] * (n)
        self.cols = [0] * (n)
        self.diagonal = 0
        self.anti_diagonal = 0
        # self.board is only used for printing purposes
        self.board = []

        for i in range(n):
            st = ""
            for j in range(n):
                st += "-"
            self.board.append(st)

    # Move function will allow the players to play the game
    # for given row and col.
    def move(self, row, col, player):
        current_player = -1
        if player == 1:
            current_player = 1

        self.rows[row] += current_player
        self.cols[col] += current_player

        if row == col:
            self.diagonal += current_player

        if col == (len(self.cols) - row - 1):
            self.anti_diagonal += current_player

        st = list(self.board[row])
        st[col] = str(current_player)
        
        st = list(self.board[row])
        if current_player == 1:
            st[col] = "O"
        else:
            st[col] = "X"
        self.board[row] = "".join(st)

        n = len(self.rows)

        if abs(self.rows[row]) == n or abs(self.cols[col]) == n or abs(self.diagonal) == n or abs(self.anti_diagonal) == n:
            return player
        return 0