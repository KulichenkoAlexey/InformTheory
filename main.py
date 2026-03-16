from greedy import greedy_alg
from graph import generate_test_graph
from drawing_graph import draw_graph

G, coords = generate_test_graph(30)
edges = greedy_alg(G)
print(edges)

draw_graph(coords, edges)


