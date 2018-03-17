import sys
sys.path.insert(0, '../')

import unittest
import dijkstra
import prim

print(dijkstra)

class DijkstraUnitTests(unittest.TestCase):

    def test_simple_graph_dijkstra(self):

        S = {0, 1, 2, 3}
        A = {
            (0, 1): 1,
            (1, 0): 1,
            (0, 2): 1,
            (2, 0): 1,
            (1, 3): 5,
            (3, 1): 5,
            (1, 2): 1,
            (2, 1): 1,
            (1, 3): 1,
            (3, 1): 1,
            (2, 3): 1,
            (3, 2): 1
        }
        distances, predecessors = dijkstra.dijkstra(S, A, 0)
        self.assertEqual(distances[3], 2)

    def test_simple_graph_prim(self):

        S = {0, 1, 2, 3}
        A = {
            (0, 1): 2,
            (1, 0): 2,
            (0, 2): 1,
            (2, 0): 1,
            (1, 2): 2,
            (2, 1): 2,
            (2, 3): 3,
            (3, 2): 3
        }
        distances, predecessors = prim.prim(S, A, 0)
        self.assertEqual(distances, {0: 0, 1: 2, 2: 1, 3: 3})
        self.assertTrue(predecessors == {
                        0: None, 1: 0, 2: 0, 3: 2} 
                        or 
                        predecessors == {0: None, 1: 2, 2: 0, 3: 2})


if __name__ == '__main__':
    unittest.main()
