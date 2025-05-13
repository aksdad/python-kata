from __future__ import annotations
from typing import Optional, List
import unittest

class Solution:
    def bubble_sort(self, nums: Optional[List[int]]):
        pass

class TestBubbleSort(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_unsorted_list(self):
        nums = [5, 2, 9, 1, 5, 6]
        self.solution.bubble_sort(nums)
        self.assertEqual(nums, [1, 2, 5, 5, 6, 9])

    def test_sorted_list(self):
        nums = [1, 2, 3, 4, 5]
        self.solution.bubble_sort(nums)
        self.assertEqual(nums, [1, 2, 3, 4, 5])

    def test_reverse_list(self):
        nums = [5, 4, 3, 2, 1]
        self.solution.bubble_sort(nums)
        self.assertEqual(nums, [1, 2, 3, 4, 5])

    def test_list_with_duplicates(self):
        nums = [3, 3, 2, 1, 2]
        self.solution.bubble_sort(nums)
        self.assertEqual(nums, [1, 2, 2, 3, 3])

    def test_empty_list(self):
        nums = []
        self.solution.bubble_sort(nums)
        self.assertEqual(nums, [])

    def test_single_element(self):
        nums = [42]
        self.solution.bubble_sort(nums)
        self.assertEqual(nums, [42])

    def test_none_input(self):
        # Should not raise an exception
        self.solution.bubble_sort(None)

if __name__ == '__main__':
    unittest.main()

