from typing import List

def selectionsort(arr: List[int]):
    """
    Description
    -----------
    Selection sort is an in-place sorting algorithm.
    With 2 for loops, select next minimun value in unsorted array
    and swap with current value.
    Time complexity is O(n^2)
    
    Parameter
    ---------
    arr: `List[int]`

    Example
    -------
    >>> from random import shuffle
    >>> a = [i for i in range(10)]
    >>> shuffle(a)
    >>> selectionsort(a)
    >>> print(a) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    """
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
