# coding: utf-8
import logging
from priority_dict import priority_dict

logging.basicConfig(level=logging.INFO)

def dijkstra(S, A, sdeb):
    edges = set(A.keys())
    distances = {x: float("inf") for x in S}
    distances[sdeb] = 0
    distances = priority_dict(distances)
    final_distance = {}
    predecessors={ x : None for x in S }
    while len(distances) != 0:       
        a = distances.smallest()
        min_dist = distances[a]
        distances.pop_smallest()
        final_distance[a] = min_dist
        voisins = [b for b in distances.keys() if (a, b) in edges]
        for b in voisins:
            distance_through_a = final_distance[a] + A[(a, b)]
            if distances[b] > distance_through_a:
                distances[b] = distance_through_a
                predecessors[b] = a
        

    return final_distance, predecessors

