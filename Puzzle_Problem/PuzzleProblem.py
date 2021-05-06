from Problem import *

nodes_depth  = 0 # Variável global para contagem de nós na busca em profundidade iterativa
nodes_a_star = 0 # Variável global para contagem de nós na busca A*
fator_depth  = 0 # Variável global para fator de ramificação na busca em profundidade iterativa
fator_a_star = 0 # Variável global para para fator de ramificação na busca A*

class PuzzleProblem(Problem): # Classe especificando o problema
    def goal_test(state):
        return state == [1, 2, 3, 4, 5, 6, 7, 8, 0]

    def __init__(self, initial_state):
        self.actions = ['T', 'B', 'L', 'R']
        super().__init__(initial_state, self.actions, PuzzleProblem.goal_test)

def problemGenerator(goal, n): # Função geradora de problemas, baseado em busca em largura
    node = Node(goal, None, None, 0)
    nivel_atual = node.path_cost
    actions = ['T', 'B', 'L', 'R']

    if nivel_atual == n:
        return node.state

    frontier = [node]
    explored = []

    while len(frontier) != 0:
        node = frontier.pop(0)
        children = expand(node, actions, move)
        explored.append(node.state)

        for child in children:
            if not ( checkIn(child.state, frontier) or child.state in explored ):
                nivel_atual = child.path_cost

                if nivel_atual == n:
                    return PuzzleProblem(child.state)

                frontier.append(child)

    return None #search fail

def lim_depth_search(problem, lim): # Busca em profundidade com aprofundamento iterativo
    global nodes_depth
    nodes_depth = 1

    for i in range(1,lim):
        result = depth_search(Node(problem.initial_state, None, None, 0), problem, i)

        if result is not None:
            print(nodes_depth, ' nós gerados. Custo: ', result.path_cost, end='.')
            return getSolutionPath(result)

    return None

def depth_search(node, problem, lim): # Busca em profundidade limitada recursiva
    global nodes_depth
    nodes_depth += 1

    if problem.goalTest(node.state):
        return node

    if (lim <= 0):
        return None

    for action in problem.actions:
        child = Node(move(node.state, action), node, action, 1)
        result = depth_search(child, problem, lim-1)

        if result is not None:
            return result

    return None

def a_star_search(problem, f): # Algoritmo de busca A*
    global nodes_a_star

    node = Node(problem.initial_state, None, None, 0)
    nodes_a_star = 1

    if problem.goalTest(node.state):
        return getSolutionPath(node)

    frontier = [node]
    explored = []

    while len(frontier) != 0:
        node = frontier.pop(0)

        if problem.goalTest(node.state):
            print(nodes_a_star, ' nós gerados. Custo: ', node.path_cost, end='.')
            return getSolutionPath(node)

        explored.append(node.state)
        children = expand(node, problem.actions, move)

        for child in children:
            nodes_a_star += 1

            if child.state not in explored and child not in frontier:
                frontier.append(child)
                frontier.sort(key=f) # Estou ordenando a cada elemento inserido para simular uma PriorityQueue
            elif child in frontier:
                if f(child) < f(frontier[child]):
                    del frontier[child]
                    frontier.append(child)
                    frontier.sort(key=f)

                frontier.append(child)
                frontier.sort(key=f)

    return None #search fail

def h1(node): # Heuristica 1 para a busca A*: Quantidades de elementos na posição errada
    state = node.state
    obj = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    erros = 0

    for i in range(9):
        if (state[i] != 0 and obj[i] != state[i]):
            erros += 1

    return erros + node.path_cost

def h2(node): # Heuristica 2 para a busca A*: Soma da distância de manhattan de cada elemento para sua posição objetivo
    state = node.state
    obj = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    soma = 0

    for i in range(9):
        if (state[i] != 0):
            x_obj = obj.index(state[i]) % 3
            y_obj = int(obj.index(state[i]) / 3)
            x_atual = i % 3
            y_atual = int(i / 3)

            temp = abs(x_atual - x_obj) + abs(y_atual - y_obj)
            soma += temp

    return soma + node.path_cost

def move(state, action): # Função que recebe uma ação e um estado; retorna um estado resultante da ação referida
    position = state.index(0)
    new_state = state[:]

    if action == 'T' or action == 'B':
        if action == 'T':
            new_position = position + 3
        else:
            new_position = position - 3

        if new_position in range(9):
            new_state[new_position], new_state[position] = new_state[position], new_state[new_position]
    elif action == 'L' or action == 'R':
        position_mod = position % 3

        if action == 'L':
            new_position = position + 1
            new_position_mod = position_mod + 1
        else:
            new_position = position - 1
            new_position_mod = position_mod - 1

        if new_position_mod in range(3):
            new_state[new_position], new_state[position] = new_state[position], new_state[new_position]
    else:
        print('Ação não suportada')

    return new_state

def show_state(state): # Função auxiliar para representar graficamente o estado
    x = 0

    for i in range(3):
        for j in range(3):
            print(state[x], end = ' ')
            x += 1
        print()

    print()
