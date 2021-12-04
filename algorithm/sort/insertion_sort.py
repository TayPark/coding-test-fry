from typing import List

def insertionsort(arr: List[int]):
    """
    Description
    -----------
    Insertion sort is an in-place sorting algorithm.
    With 2 loops, insert value in unsorted array into sorted array.
    Time complexity is O(n^2)
    
    Parameter
    ---------
    arr: `List[int]`

    Example
    -------
    >>> from random import shuffle
    >>> a = [i for i in range(10)]
    >>> shuffle(a)
    >>> insertionsort(a)
    >>> print(a) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    """
    for i in range(1, len(arr)):
        insert_target = arr[i]
        j = i - 1
        while j >= 0 and insert_target < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = insert_target
