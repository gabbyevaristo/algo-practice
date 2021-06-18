# Description
"""
- Comparison based sporting algorithm
- Not stable

Time complexity:    O(nlogn) for all cases
Space complexity:   O(1)    (in place)

"""

# Process: O(n)
"""
1. Build a heap from the input data
2. Replace root (largest item) with the last item of the heap and heapify the
   tree with the reduced heap (excluding the last element, which is the largest)
3. Repeat steps above while size of heap is greater than one

    Why do it this way?
    A naive approach would be to insert each element, ony by one, however, this
    runs in O(nlogn) time: n insertions at O(logn) cost each.

Note: A max heap is used to sort the list in ascending order
"""


# Heapify the max heap rooted at index i
def heapify(arr,i,n):
    # Store index of current node and get index of left and right child
    val = i
    left, right = 2*i + 1, 2*i + 2

    # Only changes val if children are within range and their values are
    # greater than the current value
    if left < n and arr[left] > arr[val]:
        val = left
    if right < n and arr[right] > arr[val]:
        val = right

    # If val = i, the value at index i is greater than any of its two children,
    # and no swaps need to occur
    if val != i:
        arr[i], arr[val] = arr[val], arr[i]
        heapify(arr,val,n)


def heapSort(arr):
    n = len(arr)

    # Build a max heap
    """ Start from leaf nodes as they are already heaps """
    for i in range(n,-1,-1):
        heapify(arr,i,n)

    # Extract element one by one
    for i in range(n-1, 0, -1):

        # Swap root (largest element) with last element in reduced heap
        arr[i], arr[0] = arr[0], arr[i]

        # Reduce the heap by letting i = length of arr
        heapify(arr,0,i)


arr = [12, 11, 13, 5, 6, 15]
heapSort(arr)
print(arr)
