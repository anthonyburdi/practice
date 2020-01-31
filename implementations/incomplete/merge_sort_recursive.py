# merge_sort_recursive.py

# 1/31/2020, see notebook entry for more detail.

from typing import List

def merge(arr: List[int],  left: int, mid: int, right: int) -> None:
    """Merge sorted elements between left and right pointers in arr."""

    merged = []
    orig_left = left

    L = arr[left:mid + 1]
    R = arr[mid + 1:right + 1]

    # add smaller of the elements to merge together the lists
    # while left < right_of_left and mid <= right:
    #     if arr[left] <= arr[mid]:
    #         merged.append(arr[left])
    #         left += 1
    #     else:
    #         merged.append(arr[mid])
    #         mid += 1

    i = j = 0
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            merged.append(L[i])
            i += 1
        else:
            merged.append(R[j])
            j += 1

    # add any items leftover
    # while left < right_of_left:
    #     merged.append(arr[left])
    #     left += 1

    # while mid <= right:
    #     merged.append(arr[mid])
    #     mid += 1

    while i < len(L):
        merged.append(L[i])
        i += 1

    while j < len(R):
        merged.append(R[j])
        j += 1

    # reinsert sorted items to arr
    for i, item in enumerate(merged):
        arr[orig_left + i] = item


def mergesort_helper(arr: List[int], left: int, right: int) -> None:
    """Sort an array using mergesort, recursive helper function."""
    if left < right:
        mid = left + (right - left) // 2
        mergesort_helper(arr, left, mid)
        mergesort_helper(arr, mid + 1, right)
        merge(arr, left, mid, right)


def mergesort(arr: List[int]) -> None:
    """Sort an array in place using mergesort."""
    if len(arr) > 1:
        mergesort_helper(arr, 0, len(arr) - 1)


import unittest

class TestMergesort(unittest.TestCase):

    def test_small_examples(self):
        arr = [4, 1, 5, 3, 2]
        output = [1, 2, 3, 4, 5]

        mergesort(arr)

        self.assertEqual(arr, output)

        arr = [4, 1]
        output = [1, 4]

        mergesort(arr)

        self.assertEqual(arr, output)


    def test_edge_cases(self):

        arr = []
        output = []

        mergesort(arr)

        self.assertEqual(arr, output)

        arr = [4]
        output = [4]

        mergesort(arr)

        self.assertEqual(arr, output)

        arr = [-4, -1]
        output = [-4, -1]

        mergesort(arr)

        self.assertEqual(arr, output)

        arr = [-4, -1, 5, -2, 14, 3, -27, 0]
        output = [-27, -4, -2, -1, 0, 3, 5, 14]

        mergesort(arr)

        self.assertEqual(arr, output)


    def test_large_generated_examples(self):

        import random
        n = 1000
        rand_arr = [random.randint(-n, n) for _ in range(n)]
        sorted_rand_arr = sorted(rand_arr)

        mergesort(rand_arr)

        self.assertEqual(rand_arr, sorted_rand_arr)

        n = 1000000
        rand_arr = [random.randint(-n, n) for _ in range(n)]
        sorted_rand_arr = sorted(rand_arr)

        mergesort(rand_arr)

        self.assertEqual(rand_arr, sorted_rand_arr)



if __name__ == '__main__':
    unittest.main()
