import sys
sys.path.insert(0, '../')
import dijkstra_1
import random

def test_huge_graph():
    S = range(0,1000)
    A = { (x,y): random.randint(1,100) for x in S for y in S if x< y and x < 10 }
    distances = dijkstra_1.dijkstra(S, A, 0)

if __name__ == '__main__':
    import timeit
    print(timeit.timeit("test_huge_graph()", setup="from __main__ import test_huge_graph", number=100))