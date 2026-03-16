import matplotlib.pyplot as plt
import time

def draw_graph(vertices_coords, edges):
    """
    vertices_coords: словарь {vertex: (x, y)} или список [(x1,y1), (x2,y2), ...]
    edges: список кортежей [(v1, v2), ...] - индексы вершин
    """
    plt.figure(figsize=(8, 6))
    
    # Рисование ребер
    for edge in edges:
        # Получаем координаты двух вершин ребра
        x_coords = [vertices_coords[edge[0]][0], vertices_coords[edge[1]][0]]
        y_coords = [vertices_coords[edge[0]][1], vertices_coords[edge[1]][1]]
        
        plt.plot(x_coords, y_coords, 'b-', linewidth=2, alpha=0.7)
    
    # Рисование вершин
    for i, (x, y) in enumerate(vertices_coords):
        plt.plot(x, y, 'ro', markersize=10)
        plt.text(x, y, str(i), fontsize=8, ha='center', va='center', color='white')
    
    plt.axis('equal')  # равные масштабы по осям
    plt.grid(True, alpha=0.3)
    plt.title("Дерево, полученное жадным алгоритмом")
    plt.show()

