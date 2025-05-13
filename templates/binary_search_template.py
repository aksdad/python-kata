from __future__ import annotations
from typing import List, Optional
import unittest

class Solution:
    def binary_search(self, nums: Optional[List[int]], target):
        pass

class TestBinarySearch(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_target_found(self):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(self.solution.binary_search(nums, 5), 4)

    def test_target_not_found(self):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(self.solution.binary_search(nums, 10), -1)

    def test_empty_list(self):
        self.assertEqual(self.solution.binary_search([], 3), -1)

    def test_single_element_found(self):
        self.assertEqual(self.solution.binary_search([7], 7), 0)

    def test_single_element_not_found(self):
        self.assertEqual(self.solution.binary_search([7], 3), -1)

    def test_negative_numbers(self):
        nums = [-10, -5, -2, 0, 3, 8]
        self.assertEqual(self.solution.binary_search(nums, -5), 1)
        self.assertEqual(self.solution.binary_search(nums, 8), 5)

if __name__ == '__main__':
    unittest.main()

