from hw01.main import build_graph, degree_dict

edges = [(1, 2), (2, 3)]
g = build_graph(edges)
print("Graph:", g)
print("Degrees:", degree_dict(g))
