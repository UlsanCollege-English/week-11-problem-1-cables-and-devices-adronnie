def build_graph(edges, directed=False):
    graph = {}

    for u, v in edges:
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []

        graph[u].append(v)

        if not directed:
            graph[v].append(u)

    return graph


def degree_dict(graph):
    degrees = {}
    for node in graph:
        degrees[node] = len(graph[node])
    return degrees
