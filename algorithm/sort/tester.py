import unittest
from selection_sort import selectionsort
from bubble_sort import bubblesort
from random import shuffle


class BubbleSortTest(unittest.TestCase):
    def test(self):
        a = [i for i in range(100)]
        shuffle(a)
        bubblesort(a)
        self.assertEqual(a, [i for i in range(100)])

class SelectionSortTest(unittest.TestCase):
    def test(self):
        a = [i for i in range(100)]
        shuffle(a)
        selectionsort(a)
        self.assertEqual(a, [i for i in range(100)])

if __name__ == '__main__':
    unittest.main()
