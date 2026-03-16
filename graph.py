import numpy as np
from numpy import random


def generate_test_graph(n):
    coords = random.rand( n,2 )

    # Строим матрицу расстояний между рандомными координатами
    # Сразу отсечем нижнюю половину матрицы под главной диагональю
    A = np.zeros([n,n])
    for i in range(n):
        for j in range(n):
            if i == j:
                A[i,j] = 0
            else:
                A[i,j] = (coords[i,0] - coords[j,0])**2 + (coords[i,1] - coords[j,1])**2
    
    # И все
    return A, coords

def get_all_edges(G): #Возвращает список вершин без сортировки
    n = G.shape[0]
    arr = []
    for i in range(n):
        for j in range(n):
            if i<j:
                arr.append((i,j))
    return arr

def sort_edges(G, arr):
    return sorted(arr, key= lambda edge: G[edge])

