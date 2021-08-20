import numpy as np

class TicTacGame:
    def __init__(self, board = None):
        self.cnt = 0
        self.rows = [0, 0, 0]
        self.cols = [0, 0, 0]
        self.dgns = [0, 0]

        if board is None:
            self.board = np.array([
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]
            ])
        else:
            for row in range(3):
                for col in range(3):
                    if (board[row,col] != 0):
                        self.rows[row] += board[row,col]
                        self.cols[col] += board[row,col]

                        if (row == col):
                            self.dgns[0] += board[row,col]
                        if (row + col == 2):
                            self.dgns[1] += board[row,col]

                        self.cnt += 1

            self.board = np.copy(board)

    def __str__(self):
        return str(self.board)


    def get_board(self):
        return self.board

    def possible_actions(self, player):
        actions = []

        for row in range(3):
            for col in range(3):
                if self.board[row][col] == 0:
                    actions.append((row, col, player))

        return actions

    def play(self, action):
        row, col, player = action

        self.board[row,col] = player
        self.rows[row] += player
        self.cols[col] += player
            
        if (row == col):
            self.dgns[0] += player
        if (row + col == 2):
            self.dgns[1] += player

        self.cnt += 1

    def undo(self, action):
        row, col, player = action

        self.board[row,col] = 0
        self.rows[row] -= player
        self.cols[col] -= player
            
        if (row == col):
            self.dgns[0] -= player
        if (row + col == 2):
            self.dgns[1] -= player

        self.cnt -= 1

    def status(self):
        if (3 in self.rows or 3 in self.cols or 3 in self.dgns):
            return 1
        elif (12 in self.rows or 12 in self.cols or 12 in self.dgns):
            return -1
        elif (self.cnt < 9):
            return -2
        else:
            return 0