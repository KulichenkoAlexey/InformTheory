from graph import generate_test_graph, sort_edges, get_all_edges
import numpy as np

def greedy_alg(G):
    n = G.shape[0]
    
    # Алгоритм: сортируем все ребра по возрастанию
    # Берем минимальное ребро, если оно не создает цикл, добавляем
    
    connection_sets = [i for i in range(n)]  # Каждая вершина в своем множестве
    edges = sort_edges(G, get_all_edges(G))
    graph = []
    
    # Начинаем итерации алгоритма
    for edge in edges:  # Идем по отсортированным ребрам
        u, v = edge[0], edge[1]
        
        # Проверяем, находятся ли вершины в разных множествах
        if connection_sets[u] != connection_sets[v]:
            # Добавляем ребро в остовное дерево
            graph.append(edge)
            
            # Объединяем множества
            old_set = connection_sets[v]
            new_set = connection_sets[u]
            for i in range(n):
                if connection_sets[i] == old_set:
                    connection_sets[i] = new_set
        
        # Если все вершины в одном множестве - дерево построено
        if len(set(connection_sets)) == 1:
            break
    
    return graph