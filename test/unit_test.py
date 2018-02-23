import unittest
import sys
sys.path.insert(0, '../')
import dijkstra_1


class DijkstraUnitTests(unittest.TestCase):
    """docstring for ClassName"""
    def test_simple_graph(self):

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
        distances, predecessors = dijkstra_1.dijkstra(S, A, 0)
        print(distances)
        self.assertEqual(distances[3],2)


if __name__ == '__main__':
    unittest.main()

