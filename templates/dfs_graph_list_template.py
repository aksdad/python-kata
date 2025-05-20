from __future__ import annotations
from typing import Optional, List
import unittest

class GraphEdge:
    def __init__(self, to: int, weight: int) -> None:
        self.to = to
        self.weight = weight

class Solution:
    def dfs(self, graph: List[List[GraphEdge]], source: int, target: int) -> List[int]:
        return []

class TestWeightedAdjacencyListDFS(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        # Your graph list2
        self.graph = [
            [GraphEdge(1, 3), GraphEdge(2, 1)],                        # 0
            [GraphEdge(4, 1)],                                         # 1
            [GraphEdge(3, 7)],                                         # 2
            [],                                                        # 3
            [GraphEdge(1, 1), GraphEdge(3, 5), GraphEdge(5, 2)],      # 4
            [GraphEdge(2, 18), GraphEdge(6, 1)],                      # 5
            [GraphEdge(3, 1)]                                          # 6
        ]

    def test_path_exists(self):
        path = self.solution.dfs(self.graph, 0, 3)
        # possible paths: [0,2,3] OR [0,1,4,3]
        self.assertTrue(path == [0,2,3] or path == [0,1,4,3])

    def test_no_path(self):
        result = self.solution.dfs(self.graph, 3, 0)
        self.assertEqual(result, [])

    def test_same_node(self):
        result = self.solution.dfs(self.graph, 3, 3)
        self.assertEqual(result, [3])

    def test_path_through_cycle(self):
        path = self.solution.dfs(self.graph, 0, 6)
        # expected path must pass through 5: [0,1,4,5,6]
        self.assertEqual(path, [0,1,4,5,6])

    def test_invalid_source_or_target(self):
        self.assertEqual(self.solution.dfs(self.graph, 10, 3), [])
        self.assertEqual(self.solution.dfs(self.graph, 0, 10), [])

if __name__ == '__main__':
    unittest.main()
