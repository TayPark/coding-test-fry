from typing import List


def bubblesort(arr: List[int]):
    """
    Description
    -----------
    Bubble sort is an in-place sorting algorithm.
    With 2 for loops, check every adjacent elements, swap if former is bigger
    Time complexity is O(n^2)
    
    Parameter
    ---------
    arr: `List[int]`

    Example
    -------
    >>> from random import shuffle
    >>> a = [i for i in range(10)]
    >>> shuffle(a)
    >>> bubblesort(a)
    >>> print(a) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    """
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
