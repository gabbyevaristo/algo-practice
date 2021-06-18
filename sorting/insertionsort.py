# Description
"""
- Removes an element from input data and inserts it into correct position in sorted list
- Comparison based sorting algorithm
- Entries are sorted from front to back

Advantages:
    - Efficient for small data
    - Stable
    - Used when array is small (low overhead) or when array is almost sorted (adaptiveness)
    - More efficient than bubble and selection sort (same worst case complexity)

Time complexity:
    Best case       O(n)
    Average case    O(n^2)
    Worst case      O(n^2)  (occurs when array is reverse sorted)

    - Takes (n^2)/4 comparisons and (n^2)/8 swaps in average case and double in worst case

Space complexity:   O(1)    (in-place algorithm)

"""


# Shell sort
"""
- Generalized version of insertion sort
- Uses a gap to allow elements to be moved further than just one position, like in insertion
  sort - in the last iteration, the gap reduces to 1 (insertion sort)

Time complexity:
    Best case       O(nlogn)
    Average case    O((nlogn)^2)
    Worst case      O((nlogn)^2)

"""


def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]

        # Move elements that are greater than key to one position ahead
        # of their current position
        j = i-1     # Index before current index
        while j >= 0 and key < arr[j] :
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key


arr = [32,1,21,6,3]
insertionSort(arr)
print(arr)
