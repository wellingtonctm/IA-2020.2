class Node: # Classe representando nó convencional semelhante a criada pelo professor
    def __init__(self, state, parent, action, step_cost):
        self.state = state
        self.parent = parent
        self.action = action

        if parent is not None:
            self.path_cost = parent.path_cost + step_cost
        else:
            self.path_cost = step_cost

class Problem: # Classe representando problema geral semelhante a criada pelo professor
    def __init__(self, initial_state, actions, goal_test):
        self.initial_state = initial_state
        self.actions = actions
        self.goalTest = goal_test

def checkIn(state, nodeList): # Função que checa se existe um nó existe em determinada lista semelhante a do professor
    for node in nodeList:
        if state == node.state:
            return True

    return False

def getSolutionPath(node): # Função que gera o caminho de solução a partir do nó objetivo semelhante a do professor
    path = []

    while node.parent != None:
        path.append(node.action)
        node = node.parent

    path.reverse()
    return path

def expand(node, actions, move): # Função que expande um dado nó com todas as ações possíveis semelhante a do professor
    children = []

    for action in actions:
        state = move(node.state, action)

        if state is not None:
            children.append(Node(state, node, action, 1))

    return children
