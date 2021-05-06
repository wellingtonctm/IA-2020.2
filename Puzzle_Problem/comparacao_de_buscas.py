from PuzzleProblem import *
import time

def time_comp(problem, n):
    print('Tamanho do problema: ', n)
    print('A*(h1): ', end='')
    ini = time.time()
    solucao = a_star_search(problem, h1)
    fim = time.time()
    print(' Tempo: ', round(fim-ini, 10))

    print('A*(h2): ', end='')
    ini = time.time()
    solucao = a_star_search(problem, h2)
    fim = time.time()
    print(' Tempo: ', round(fim-ini, 10))

    if (n <= 10):
        print('BAI: ', end='')
        ini = time.time()
        solucao = lim_depth_search(problem, 50)
        fim = time.time()
        print(' Tempo: ', round(fim-ini, 10))

state = [1, 2, 3, 4, 5, 6, 7, 8, 0]

# Comparação do tempo dos algoritmos
for n in range(2, 10, 2):
    problem = problemGenerator(state, n)
    time_comp(problem, n)
    print()
