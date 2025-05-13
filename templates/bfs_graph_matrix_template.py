import unittest

class Solution:
    # graph = weightedadjacencymatrix = [int][int]
    def bfs(self, graph, source, target):
        return []

class TestBFS(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_found(self):
        graph = [
            [0, 1, 0],
            [0, 0, 1],
            [0, 0, 0]
        ]
        self.assertEqual(self.solution.bfs(graph, 0, 2), [0, 1, 2])

    def test_not_found(self):
        graph = [
            [0, 1, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        self.assertIsNone(self.solution.bfs(graph, 0, 2))

    def test_same_node(self):
        graph = [
            [0]
        ]
        self.assertEqual(self.solution.bfs(graph, 0, 0), [0])

    def test_empty_graph(self):
        graph = []
        self.assertIsNone(self.solution.bfs(graph, 0, 1))

    def test_cycle(self):
        graph = [
            [0, 1, 0],
            [0, 0, 1],
            [1, 0, 0]
        ]
        path = self.solution.bfs(graph, 0, 2)
        # valid paths: [0,1,2]
        self.assertEqual(path, [0,1,2])

    def test_disconnected(self):
        graph = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        self.assertIsNone(self.solution.bfs(graph, 0, 1))
        self.assertIsNone(self.solution.bfs(graph, 1, 2))

if __name__ == "__main__":
    unittest.main()
