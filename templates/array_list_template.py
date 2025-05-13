import unittest

class ArrayList:
    length = 0

    def prepend(self, item):
        pass

    def insert_at(self, item, idx):
        pass

    def append(self, item):
        pass

    def remove(self, item):
        pass

    def get(self, idx):
        pass

    def removeAt(self, idx):
        pass

class TestArrayList(unittest.TestCase):
    def setUp(self):
        self.array = ArrayList()

    def test_append(self):
        self.array.append(1)
        self.assertEqual(self.array.get(0), 1)
        self.assertEqual(self.array.length, 1)

    def test_prepend(self):
        self.array.append(2)
        self.array.prepend(1)
        self.assertEqual(self.array.get(0), 1)
        self.assertEqual(self.array.get(1), 2)
        self.assertEqual(self.array.length, 2)

    def test_insert_at(self):
        self.array.append(1)
        self.array.append(3)
        self.array.insert_at(2, 1)
        self.assertEqual(self.array.get(0), 1)
        self.assertEqual(self.array.get(1), 2)
        self.assertEqual(self.array.get(2), 3)

    def test_remove(self):
        self.array.append(1)
        self.array.append(2)
        self.array.append(3)
        self.array.remove(2)
        self.assertEqual(self.array.length, 2)
        self.assertEqual(self.array.get(0), 1)
        self.assertEqual(self.array.get(1), 3)

    def test_remove_at(self):
        self.array.append(1)
        self.array.append(2)
        self.array.append(3)
        self.array.removeAt(1)
        self.assertEqual(self.array.length, 2)
        self.assertEqual(self.array.get(0), 1)
        self.assertEqual(self.array.get(1), 3)

    def test_get_out_of_bounds(self):
        with self.assertRaises(IndexError):
            self.array.get(0)

    def test_remove_nonexistent_item(self):
        self.array.append(1)
        with self.assertRaises(ValueError):
            self.array.remove(2)

if __name__ == '__main__':
    unittest.main()
