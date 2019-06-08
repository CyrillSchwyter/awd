from unittest import TestCase

from sortierungen.Sort import BubbleSort
from sortierungen.Sort import MergeSort


class TestSort(TestCase):
    def test_sort(self):
        bubbleSort = BubbleSort()
        list_to_sort = [1, 2]
        list_to_check = [1, 2]

        # list_to_sort = [6, 2, 1]
        # list_to_check = [1, 2, 6]

        bubbleSort.sort(list_to_sort)
        self.assertEqual(list_to_check, list_to_sort, "nicht gleich")

    def test_sort_Merge(self):
        merge = MergeSort()
        # list_to_sort = [1, 2]
        # list_to_check = [1, 2]

        list_to_sort = [6, 2, 1, 7, 3, 11, 10]
        list_to_check = [1, 2, 3, 6, 7, 10, 11]

        res = merge.sort(list_to_sort)
        self.assertEqual(list_to_check, res, "nicht gleich")
