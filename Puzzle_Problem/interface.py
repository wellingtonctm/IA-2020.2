from PuzzleProblem import *

n = int(input('Tamanho do problema: '))
state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
problem = problemGenerator(state, n)

solucao = a_star_search(problem, h2)
print('Solução:', solucao)

if solucao is not None:
    print('Initial state:')
    state = problem.initial_state
    show_state(state)

    for action in solucao:
        print('Ação: ', action)
        state = move(state, action)
        show_state(state)
else:
    print('Falha na Busca')
