# Description
"""
- Efficient in determining whether a list is already sorted or not
- Elements are sorted from back to front

Time complexity:
    Best case       O(n)    (if flag is used)
    Average case    O(n^2)
    Worst case      O(n^2)  (occurs when array is reverse sorted)

    - Takes (n^2)/2 comparisons and (n^2)/2 swaps in average and worst case

Space complexity:   O(1)    (in-place algorithm)

"""


# Runs in O(n^2) time even in best case
def bubbleSort(arr):
    for i in range(len(arr)):
        # For each iteration i, j decreases by 1 as last element is
        # placed at the correct index
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


# Runs in O(n) in best case (when elements are sorted already)
""" If swapped remains false in the first pass, it means elements no elements
were swapped and the list is already sorted """
def bubbleSortOptimized(arr):
    for i in range(len(arr)):
        swapped = False
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True      # Change flag is elements have been swapped
        if swapped == False:
            break


arr = [32,1,21,6,3]
bubbleSort(arr)
print(arr)
