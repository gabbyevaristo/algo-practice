# Search an element in a sorted rotated array
def searchInRotatatedArray(arr,key):
    low, high = 0, len(arr)-1

    while low <= high:
        mid = (low + high) / 2

        if arr[mid] == key:
            return mid

        # If the left half is the greater sorted portion
        if arr[low] <= arr[mid]:
            # If key is within greater portion range,
            # search left, else search right
            if key >= arr[low] and key < arr[mid]:
                high = mid-1
            else:
                low = mid+1

        # If the right half is the smaller sorted portion
        else:
            # If key is within smaller portion range,
            # search right, else search left
            if key > arr[mid] and key <= arr[high]:
                low = mid+1
            else:
                high = mid-1
    return -1


# Find element that appears only once in a sorted array
""" All elements before target have the first occurrence at an even index
and next occurrence at an odd index, and all elements after target have
first occurrence at an odd index and next occurrence at an even index. If
mid is even, compare it to mid+1 - if they are equal, search the right,
else search the left. If mid is odd, compare it to mid-1 - if they are
equal, search the right, else search the left. """
def oneOccurrence(arr):
    low, high = 0, len(arr)-1

    while low <= high:
        if low == high:
            return arr[low]

        mid = (low + high) / 2

        # If mid is even and element next to mid is equal to it,
        # bypass both elements and search right. Else, mid is
        # still a possibility, so include it in the search left.
        if mid % 2 == 0:
            if arr[mid] == arr[mid+1]:
                low = mid+2
            else:
                high = mid
        # If mid is odd and element previous to mid is equal
        # to it, then bypass mid element and search right.
        # Else, mid is not a possibility and search left.
        else:
            if arr[mid] == arr[mid-1]:
                low = mid+1
            else:
                high = mid-1


# Find maximum value in an increasing then decreasing array
def findMaximum(arr):                                   # O(logn)
    low, high = 0, len(arr)-1

    while low <= high:
        # If there is only one element
        if low == high:
            return arr[low]

        # If there are two elements, take the maximum one
        if low == high-1:
            return max(arr[low],arr[high])

        mid = (low + high) / 2

        # Return arr[mid] if it is greater than both its neighbors
        if arr[mid] > arr[mid+1] and arr[mid] > arr[mid-1]:
            return arr[mid]

        # If arr[mid] is greater than the next element and smaller
        # than the previous element, then we are in the decreasing
        # half and maximum exists on the left half. Else, we are in
        # the increasing half and maximum exists on the right half.
        if arr[mid] > arr[mid+1] and arr[mid] < arr[mid-1]:
            high = mid-1
        else:
            low = mid+1


# Given a SORTED array and a value x, find the ceiling of x (ceiling of x is
# the smallest element in the array greater than or equal to x)
""" Can find the floor of x by traversing the array backwards and returning
arr[i] when x > arr[i]. """
def findCeiling(arr,x):
    # Ceiling does not exist if greatest value in array is less than x
    if arr[-1] < x:
        return -1

    # If current element is greater than x, return it
    for i in range(len(arr)):
        if arr[i] == x:
            return arr[i]
        if arr[i] > x:
            return arr[i]

""" Using binary search reduces the time complexity to O(logn) """
def findCeiling2(arr,x):
    low, high = 0, len(arr)-1

    while low < high:
        # Return first element if x is smaller than or equal to it
        if x <= arr[low]:
            return arr[low]

        # Return -1 if x is greater than the last element
        if x > arr[high]:
            return -1

        mid = (low + high) / 2

        # Return arr[mid] if x is equal to it
        if x == arr[mid]:
            return arr[mid]

        # If x is greater than arr[mid], then either arr[mid+1]
        # is the ceiling or the ceiling lies in arr[mid+1...high]
        elif x > arr[mid]:
            if mid+1 <= high and x <= arr[mid+1]:
                return arr[mid+1]
            else:
                low = mid+1

        # If x is smaller than arr[mid], then either arr[mid]
        # is the ceiling or the ceiling lies in arr[low...mid-1]
        # NOTE - Can also just set high = mid. If x is less than mid,
        # then it is still possible for mid to be the ceiling of x.
        else:
            if mid-1 >= low and x > arr[mid-1]:
                return arr[mid]
            else:
                high = mid-1


# Given a sorted array, find the index of the first occurrence of a number
def firstOccurrence(arr,data):
    low, high = 0, len(arr)-1

    while low <= high:
        # If data is not in range
        if data < arr[low] or data > arr[high]:
            return -1

        mid = (low + high) / 2

        if (mid == low and arr[mid] == data) or (arr[mid] == data and arr[mid-1] < data):
            return mid

        # If data is greater than the middle element,
        # search the right side. Else, search the left.
        if data > arr[mid]:
            low = mid+1
        else:
            high = mid-1


# Find only repeating element in a sorted array, where all elements are
# in the range from 1 to n
def findRepeatingElement(arr):
    low, high = 0, len(arr)-1

    while low <= high:
        mid = (low + high) / 2

        # If middle element is not in its proper position,
        # repeating element is either the current middle
        # element or its on the left half
        if arr[mid] != mid + 1:
            if mid > 0 and arr[mid] == arr[mid-1]:
                return mid
            high = mid-1

        # If middle element is in its proper position,
        # repeating element is on the right side
        else:
            low = mid+1


# Given a list of n-1 integers with values in range 1 to n, find the missing number
"""
Method 1: Add all array values to a set. Iterate from 1 to n+1, and
          return once i is not in the set.
Method 2: Sort the array. Iterate through the array, and return i+1
          if arr[i] != i+1.
"""
def findMissingNumber(arr):
    x1, x2 = arr[0], 1
    for i in range(1,len(arr)):         # xor all elements in array
        x1 ^= arr[i]

    for j in range(2, len(arr)+2):      # xor all elements from 1 to n
        x2 ^= j

    # All elements seen twice will cancel out, and the
    # missing number (only seen in range) will remain
    return x1 ^ x2


# Given an array, find all peak elements (an element is peak if it is greater than
# or equal to its neigbors)
def findPeak(arr):                                      # O(n)
    res = []

    # If first element is greater than or equal
    # to second element, first element is a peak
    if arr[0] >= arr[1]:
        res.append(arr[0])

    # If last element is greater than or equal to
    # second to last element, last element is a peak
    if arr[-1] >= arr[-2]:
        res.append(arr[-1])

    # Narrow traversal since corner cases were accounted for.
    # If current element is greater than or equal to its
    # neighbors, append it to result array.
    for i in range(1,len(arr)-1):
        if arr[i] >= arr[i-1] and arr[i] >= arr[i+1]:
            res.append(arr[i])
    return res

""" Using binary search reduces the time complexity to O(logn), though the
method below only finds one peak, not all of them """
def findPeak2(arr):
    low, high = 0, len(arr)-1

    while low < high:
        mid = (low + high) / 2

        # Return arr[mid] if it is greater than or equal to its neighbors
        if arr[mid] >= arr[mid+1] and arr[mid] >= arr[mid-1]:
            return arr[mid]

        # If the middle element is smaller than its left neighbor, there is
        # always a peak in the left half. The same goes for the right.
        if arr[mid] < arr[mid+1]:
            low = mid+1
        else:
            high = mid-1
    return arr[low]

""" Similar to method above, without extra conditions """
def findPeak3(arr):
    low, high = 0, len(arr)-1

    while low < high:
        mid = (low + high) / 2

        # If the middle element is smaller than its left neighbor, there is
        # always a peak in the left half (arr[mid+1...high]). If the middle
        # element is greater than its neighbor, then the middle element is
        # a possible peak (arr[low...mid]).
        if arr[mid] < arr[mid+1]:
            low = mid+1
        else:
            high = mid
    return arr[low]


arr = [2,2,4,5,5,6,6,7,7]
print(oneOccurrence(arr))
