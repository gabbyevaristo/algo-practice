# Types of searching
"""
1. Unordered linear search
    - Typical search where elements are not sorted
    - Time complexity:
            O(n) in the worst case (if target is not in list)


2. Sorted/ordered linear search
    - At any point, if the value at A[i] is greater than the target, then
      return -1 without searching the remaining array
    - Can further improve performance by checking if target is less than
      arr[0] or greater than arr[-1] before the loop, and if so, returning
      False
    - Time complexity:
            O(n) in the worst case, but reduced in the average case

        def sortedSearch(arr,target):
            for i in range(len(arr)):
                if A[i] == target:
                    return i
                else if A[i] > target:
                    return -1
            return -1


3. Binary search
    - Time complexity:  O(logn)


4. Interpolation search
    - Improvement over binary search where elements in sorted array are
      uniformly distrubuted
    - If target is closer to the last element, for example, this search
      is likely to create a "mid" closer to the last element
    - Time complexity:
            O(loglogn) if distributed uniformly, else O(n)

    - Position equation:
        position = low + int((float(high - low) /
            (arr[high] - arr[low])) * (x - arr[low]))


5. Jump search
    - Jumps array in fixed block sizes - once it reaches a step value
      greater than the target, it jumps backwards and performs a linear
      search until target is found or next block is reached
    - Best step size = sqrt(n)
    - Main advantage over binary search is that it traverses back only once
    - Time complexity:
            O(sqrt(n))  (faster than linear, but slower than binary)

6. Exponential search
    - Finds range where target is present by repeated doubling, then
      performs binary search on that range
    - Useful for unbounded searches where array size is infinite
    - Time/space complexity:  O(logn)


7. BSTs
    - Time complexity:
            O(logn) on average, but O(n) for skewed trees


8.  Symbol tables and hashing

9. String searching algorithms (tries, ternary search, suffix trees)

    Ternary search
        - Similar to binary search, instead the array is divided into three
        - Time complexity: O(log[base 3]n)

"""


# Linear search using two pointers
def linearSearch(arr,target):
    i, j = 0, len(arr)-1

    # If arr[i] or arr[j] is equal to target, return the appopriate
    # index. Else, increment i and decrement j.
    while i < j:
        if arr[i] == target:
            return i
        elif arr[j] == target:
            return j
        else:
            i += 1
            j -= 1
    return -1
