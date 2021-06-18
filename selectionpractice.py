# Find smallest and largest value in the given array
"""
Best case:  n-1 comparisons (array is in ascending order)
Worst case: 2(n-1) comparisons (array is in descending order)
"""
def findSmallestAndLargest(arr):
    small = large = arr[0]

    # Compare current element to min
    # only if comparison to max fails
    for i in range(1,len(arr)):
        if arr[i] > large:
            large = arr[i]
        elif arr[i] < small:
            small = arr[i]
    return (small,large)


""" Compares values in pairs and manipulates iteration range depending
on the array length (even or odd). """
def findSmallestAndLargest2(arr):
    small, large = float('inf'), float('-inf')

    # If array length is odd, n is set to
    # array length-1 and odd is set to True
    odd = False
    if len(arr) % 2 == 1:
        n, odd = len(arr)-1, True
    else:
        n = len(arr)

    # Traverses array up to n, depending
    # if array length is even or odd
    for i in range(0,n,2):          # Step size = 2

        # If current element is less than next element,
        # check if it is less than small and check if
        # next element is greater than large
        if arr[i] < arr[i+1]:
            if arr[i] < small:
                small = arr[i]
            if arr[i+1] > large:
                large = arr[i+1]

        # If current element is greater than next element,
        # check if it is greater than large and check if
        # next element is less than small
        else:
            if arr[i] > large:
                large = arr[i]
            if arr[i+1] < small:
                small = arr[i+1]

    # If array length is odd, check if the
    # last element is a maximum or minimum
    if odd:
        if arr[-1] > large:
            large = arr[-1]
        elif arr[-1] < small:
            small = arr[-1]

    return (small,large)


# Print the k smallest elements in the given array
""" Method is selection sort. Time complexity = O(k*n). """
def printKSmallet(arr,k):
    for i in range(len(arr)):             # Runs k times
        minIndex = i

        # At the end of this loop, minIndex will be the
        # index of the minimum value in the reduced list
        for j in range(i+1,len(arr)):

            # If element is less than current minimum value,
            # set minimum index to current index
            if arr[j] < arr[minIndex]:
                minIndex = j

        # Print smallest element k times
        if k > 0:
            print(arr[minIndex], end=" ")
            k -= 1

        arr[i], arr[minIndex] = arr[minIndex], arr[i]


# Other methods to print k smallest elements
"""
1. Sort and print first k elements

        O(nlogn) to sort and O(k) to print k elements
            = O(nlogn + k) ~ O(nlogn)

----------------------------------------------------------------------------

2. Insert elements into a BST and perform an inorder traversal, printing
   k elements

        O(nlogn) to create a BST and O(k) to print k elements
            = O(nlogn + k) ~ O(nlogn)

        Note: If elements are in a sorted order, tree will be skewed,
              giving an O(n) time complexity.

----------------------------------------------------------------------------

3. Place the first k elements into a max heap. Add the next values into the
   heap one by one. If the value is larger than the root, return. If it is
   smaller than the root, remove the root, add the new element, and heapify
   the heap. At the end of the traversal, the smallest k elements will still
   be in the heap.

        O(klogk) to create a heap for first k elements and O((n-k)logk)
        to add the rest of the elements [ O(logk) for one element ]
            = O(klogk + (n-k)logk) ~ O(nlogk)

"""

arr = [4,10,2,9,12,3,22,11,5,5]
print(printKSmallet(arr, 4))
