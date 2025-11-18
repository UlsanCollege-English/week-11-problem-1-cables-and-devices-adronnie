def build_graph(edges, directed=False):
    graph = {}

    for u, v in edges:
        # Ensure nodes exist
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []

        # Add edge u → v
        graph[u].append(v)

        # Add reverse edge if undirected
        if not directed:
            graph[v].append(u)

    return graph


def degree_dict(graph):
    # Return a new dictionary mapping each node to its degree
    return {node: len(neighbors) for node, neighbors in graph.items()}
