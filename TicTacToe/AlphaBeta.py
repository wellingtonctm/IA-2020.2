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
                row, col, _ = self.minimax_alpha_beta()

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

    def minimax_alpha_beta(self):
        alpha = -inf
        beta = inf
        best_action, _ = self.max_choice(alpha, beta)
        return best_action

    def max_choice(self, alpha, beta):
        status = self.game.status()

        if status > -2:
            return None, status

        value = -inf
        actions = self.game.possible_actions(X)
        best_action = None

        for action in actions:
            self.game.play(action)
            _, min_val = self.min_choice(alpha, beta)
            self.game.undo(action)

            if min_val > value:
                value = min_val
                best_action = action

            if value >= beta:
                return best_action, value

            alpha = max(value, alpha)

        return best_action, value

    def min_choice(self, alpha, beta):
        status = self.game.status()

        if status > -2:
            return None, status

        value = inf
        actions = self.game.possible_actions(O)
        best_action = None

        for action in actions:
            self.game.play(action)
            _, max_val = self.max_choice(alpha, beta)
            self.game.undo(action)

            if max_val < value:
                value = max_val
                best_action = action

            if value <= alpha:
                return best_action, value

            beta = min(value, beta)

        return best_action, value