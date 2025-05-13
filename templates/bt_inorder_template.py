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
    def inorder(self, head: Optional[Node]):
        pass

class TestInOrderBinaryTree(unittest.TestCase):
    def setUp(self):
        """
        Tree used for testing:
                 5
               /   \
              3     8
             / \\   / \
            1   4 7   9
        In-order traversal: [1, 3, 4, 5, 7, 8, 9]
        """
        self.root = Node(5,
                         Node(3, Node(1), Node(4)),
                         Node(8, Node(7), Node(9))
                         )
        self.solution = Solution()

    def test_inorder_traversal(self):
        expected = [1, 3, 4, 5, 7, 8, 9]
        result = self.solution.inorder(self.root)
        self.assertEqual(result, expected)

    def test_empty_tree(self):
        result = self.solution.inorder(None)
        self.assertEqual(result, [])

    def test_single_node(self):
        single = Node(42)
        result = self.solution.inorder(single)
        self.assertEqual(result, [42])

if __name__ == '__main__':
    unittest.main()
