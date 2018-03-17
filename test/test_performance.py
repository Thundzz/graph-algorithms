import sys
sys.path.insert(0, '../')

import unittest
import dijkstra
import random
from datetime import datetime

def millis_interval(start, end):
    """start and end are datetime instances"""
    diff = end - start
    millis = diff.days * 24 * 60 * 60 * 1000
    millis += diff.seconds * 1000
    millis += diff.microseconds / 1000
    return millis

class PerformanceTest(unittest.TestCase):

    def test_simple_graph_dijkstra(self):
        tick = datetime.now()
        for i in range(100):
            S = range(0,100)
            A = { (x,y): random.randint(1,100) for x in S for y in S if x< y and x < 10 }

            distances = dijkstra.dijkstra(S, A, 0)
        
        tock = datetime.now()   
        assert(millis_interval(tick, tock) <= 350)

# def test_huge_graph():
#     S = range(0,100)
#     A = { (x,y): random.randint(1,100) for x in S for y in S if x< y and x < 10 }
#     distances = dijkstra.dijkstra(S, A, 0)

# if __name__ == '__main__':
#     duration = timeit.timeit("test_huge_graph()", setup="from __main__ import test_huge_graph", number=100)
#     assert(duration <= 1)

if __name__ == '__main__':
    unittest.main()
