# Time complexity: O(sqrt(n))

import math

def jumpSearch(arr,target):
    # Get step size
    step = math.sqrt(len(arr))
    prev = 0

    # Finds block where target is present (if present)
    """ -1 is returned here when target is greater than
    the last element in the array """
    while arr[int(min(step,len(arr)))-1] < target:
        prev = step
        step += math.sqrt(len(arr))
        if prev >= len(arr):
            return -1

    # Perform a linear search for target in block
    # beginning with prev
    while arr[int(prev)] < target:
        prev += 1

        # If next block or end of array is reached,
        # target is not present
        if prev == min(step,len(arr)):
            return -1

    # If target is at prev index, return it
    if arr[int(prev)] == target:
        return int(prev)
    return -1


arr = [1,3,5,6,7,9,10]
print(jumpSearch(arr, 7))
