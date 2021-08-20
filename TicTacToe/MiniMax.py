from TicTacGame import TicTacGame

X = 1 # MAX
O = 4 # MIN
inf = 2

class AiTicTac:
    def __init__(self, turn = 'X'):
        self.turn = 0 if turn == 'X' else 'O'
        self.game = TicTacGame()
        self.info = 'Turn: {}'.format(turn)

    def get_info(self):
        return self.info

    def get_position(self, row, col):
        pos = self.game.get_board()[row][col]

        if pos == 0:
            return ' '
        elif pos == 1:
            return 'X'
        else:
            return 'O' 

    def play(self, row = -1, col = -1):
        if self.turn == 0:
            if (row == -1 or col == -1):
                row, col, _ = self.minimax_decision()

            self.game.play((row, col, X))
            self.info = 'Turn: {}'.format('O')
            self.turn = 1
        else:
            self.game.play((row, col, O))
            self.info = 'Turn: {}'.format('X')
            self.turn = 0

        return row, col

    def status(self):
        status = self.game.status()

        if status > -2:
            if status == 1:
                self.info = 'X'
            elif status == -1:
                self.info = 'O'
            else:
                self.info = 'Nobody'

            return True

        return False

    def minimax_decision(self):
        actions = self.game.possible_actions(X)
        value = -inf
        best_action = None

        for action in actions:
            self.game.play(action)
            aux = self.min_value()
            self.game.undo(action)

            if (aux > value):
                value = aux
                best_action = action

        return best_action

    def min_value(self):
        status = self.game.status()

        if status > -2:
            return status
        
        actions = self.game.possible_actions(O)
        value = inf

        for action in actions:
            self.game.play(action)
            aux = self.max_value()
            self.game.undo(action)

            if (aux < value):
                value = aux

        return value

    def max_value(self):
        status = self.game.status()

        if status > -2:
            return status
        
        actions = self.game.possible_actions(X)
        value = -inf

        for action in actions:
            self.game.play(action)
            aux = self.min_value()
            self.game.undo(action)

            if (aux > value):
                value = aux

        return value
