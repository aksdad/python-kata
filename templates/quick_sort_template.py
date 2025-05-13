import unittest

class Solution:
    def quick_sort(self, nums):
        pass

class TestQuickSort(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_list(self):
        self.assertEqual(self.solution.quick_sort([]), [])

    def test_single_element(self):
        self.assertEqual(self.solution.quick_sort([1]), [1])

    def test_sorted_list(self):
        self.assertEqual(self.solution.quick_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_reverse_sorted_list(self):
        self.assertEqual(self.solution.quick_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_random_order(self):
        self.assertEqual(self.solution.quick_sort([3, 1, 4, 1, 5, 9, 2]), [1, 1, 2, 3, 4, 5, 9])

    def test_with_duplicates(self):
        self.assertEqual(self.solution.quick_sort([2, 3, 2, 1, 4, 1]), [1, 1, 2, 2, 3, 4])

    def test_negative_numbers(self):
        self.assertEqual(self.solution.quick_sort([-3, -1, -4, 2, 0]), [-4, -3, -1, 0, 2])

if __name__ == "__main__":
    unittest.main()
