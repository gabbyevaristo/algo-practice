# Description
"""
- Not stable
- Preferred for arrays over LL
- Worst case occurs when elements are already sorted - O(n^2)

Time complexity:
    Best case       O(nlogn)
    Average case    O(nlogn)
    Worst case      O(n^2)      (can be implemented by changing pivot choice
                                 so that the worst case rarely occurs)

Space complexity:   O(1)        (qualifies as in-place since extra space
                                 is only used for recursive calls)
                    O(logn)     (if counting stack records)

Variations in choosing pivot:
    - Always pick first element as pivot
    - Always pick last element as pivot
    - Pick random element as pivot
    - Pick median as pivot

"""

# Algorithm
"""
    1. If there are one or no elements in array to be sorted, return
    2. Pick an element as pivot
    3. Split the array into two parts - one with elements larger than
       pivot and the other with elements smaller than pivot
    4. Recursively repeat algorithm for both halves of original array

"""


# Takes last element as pivot and places it in the correct position in
# sorted array by placing all elements smaller than it to its left and
# all elements greater than it to its right
def partition(arr,low,high):
    i = low-1               # Index of smaller element
    pivot = arr[high]       # Pivot = last element

    # At the end of the loop, index i will be the last smallest element
    # to the left of pivot. The pivot is then placed at index i+1.
    for j in range(low, high):

        # If current element is smaller than the pivot
        if arr[j] < pivot:

            # Increment index of smaller element and swap
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

def quickSort(arr,low,high):
    if low < high:

        # p = partitioning index, so arr[p] is now at the right place
        p = partition(arr,low,high)

        # Separately sort elements before partition and after partition
        quickSort(arr, low, p-1)
        quickSort(arr, p+1, high)


arr = [12, 11, 13, 5, 6, 15]
quickSort(arr,0,len(arr)-1)
print(arr)
