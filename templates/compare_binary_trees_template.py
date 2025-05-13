from __future__ import annotations
from typing import Optional
import unittest

class Node:
    def __init__(self, val: int, left: Optional[Node] = None, right: Optional[Node] = None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # tree1 and tree2 are root of tree
    def compare(self, tree1: Optional[Node], tree2: Optional[Node]) -> bool:
        return False

class TestCompareBinaryTrees(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_identical_trees(self):
        t1 = Node(1, Node(2), Node(3))
        t2 = Node(1, Node(2), Node(3))
        self.assertTrue(self.solution.compare(t1, t2))

    def test_different_structure(self):
        t1 = Node(1, Node(2))
        t2 = Node(1, None, Node(2))
        self.assertFalse(self.solution.compare(t1, t2))

    def test_different_values(self):
        t1 = Node(1, Node(2), Node(3))
        t2 = Node(1, Node(2), Node(4))
        self.assertFalse(self.solution.compare(t1, t2))

    def test_one_tree_none(self):
        t1 = None
        t2 = Node(1)
        self.assertFalse(self.solution.compare(t1, t2))

    def test_both_trees_none(self):
        self.assertTrue(self.solution.compare(None, None))

if __name__ == '__main__':
    unittest.main()
