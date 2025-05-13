from __future__ import annotations
from typing import Optional
import unittest

class Node:
    def __init__(self, val: int, left: Optional[Node] = None, right: Optional[Node] = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # head = root of binary tree
    def bfs(self, head: Optional[Node], target: int):
        pass

class TestBFSBinaryTree(unittest.TestCase):
    def setUp(self):
        """
        Tree used for testing:
                 5
               /   \
              3     8
             / \\   / \\
            1   4 7   9
        """
        self.root = Node(5,
                         Node(3, Node(1), Node(4)),
                         Node(8, Node(7), Node(9))
                         )
        self.solution = Solution()

    def test_found(self):
        self.assertTrue(self.solution.bfs(self.root, 7))

    def test_not_found(self):
        self.assertFalse(self.solution.bfs(self.root, 10))

    def test_root_value(self):
        self.assertTrue(self.solution.bfs(self.root, 5))

    def test_leaf_value(self):
        self.assertTrue(self.solution.bfs(self.root, 1))

    def test_empty_tree(self):
        self.assertFalse(self.solution.bfs(None, 1))

if __name__ == '__main__':
    unittest.main()
