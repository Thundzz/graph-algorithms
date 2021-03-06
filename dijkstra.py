# coding: utf-8

def dijkstra(S, A, sdeb):
    edges = set(A.keys())
    distances = {x: float("inf") for x in S}
    distances[sdeb] = 0
    remaining = S
    predecessors={ x : None for x in S }
    while bool(remaining):
        min_dist = min([distances[c] for c in remaining])
        a = next(x for x in remaining if distances[x] == min_dist)
        remaining.remove(a)
        voisins = [b for b in remaining if (a, b) in edges]
        for b in voisins:
            candidate = distances[a] + A[(a, b)]
            if distances[b] > distances[a] + A[(a, b)]:
                distances[b] = candidate
                predecessors[b] = a
        

    return distances, predecessors

