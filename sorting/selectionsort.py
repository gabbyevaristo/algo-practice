# Description
"""
Uses/pros:
    - Works well for small files
    - Used for sorting files with large values and small keys since
      selection is made based on keys
    - Never makes more than n swaps
    - Useful when memory write is costly
    - Uses minimum number of swaps between all in-place sorting algorithms

Time complexity:    O(n^2) in all cases
    - Takes (n^2)/2 comparisons and n swaps

Space complexity:   O(1)    (in-place algorithm)

"""

# Algorithm
"""
    1. Find minimum value in list
    2. Swap with value in current position
    3. Repeat process
"""


def selectionSort(arr):
    for i in range(len(arr)):
        # Set minimum index to current index
        minIndex = i

        # Iterate from next index. At the end of this loop,
        # minIndex = index of minimum value in reduced list.
        for j in range(i+1,len(arr)):

            # If element is less than current minimum value,
            # set minimum index to current index
            if arr[j] < arr[minIndex]:
                minIndex = j

        # Swap index i with minimum value
        arr[i], arr[minIndex] = arr[minIndex], arr[i]


""" This algorithm is stable as it maintains order of duplicates values
of original array """
def selectionSortStable(arr):
    for i in range(len(arr)):
        minIndex = i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j

        # Instead of swapping, index is pushed forward to correct index. Elements
        # before minimum index are moved one step backwards.
        key = arr[minIndex]
        while minIndex > i:
            arr[minIndex] = arr[minIndex-1]
            minIndex -= 1
        arr[i] = key


arr = [32,1,21,6,3]
selectionSortStable(arr)
print(arr)
