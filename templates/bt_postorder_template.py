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
    def postorder(self, head: Optional[Node]):
        pass

class TestPostOrderBinaryTree(unittest.TestCase):
    def setUp(self):
        """
        Tree used for testing:
                 5
               /   \
              3     8
             / \\   / \
            1   4 7   9
        Post-order traversal: [1, 4, 3, 7, 9, 8, 5]
        """
        self.root = Node(5,
                         Node(3, Node(1), Node(4)),
                         Node(8, Node(7), Node(9))
                         )
        self.solution = Solution()

    def test_postorder_traversal(self):
        expected = [1, 4, 3, 7, 9, 8, 5]
        result = self.solution.postorder(self.root)
        self.assertEqual(result, expected)

    def test_empty_tree(self):
        result = self.solution.postorder(None)
        self.assertEqual(result, [])

    def test_single_node(self):
        single = Node(42)
        result = self.solution.postorder(single)
        self.assertEqual(result, [42])

if __name__ == '__main__':
    unittest.main()
