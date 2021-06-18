# Given two arrays, find the pair of values with the smallest absolute difference
""" Time complexity: O(mlogm + nlogn) = O(mlogm + nlogn) to sort and O(m + n) to
                     find the mininimum difference """
def smallestAbsoluteDifference(arr1,arr2):
    arr1.sort()
    arr2.sort()

    a = b = 0
    diff = float('inf')

    while a < len(arr1) and b < len(arr2):
        # Update diff if new difference is smaller than the old one
        diff = min(diff, abs(arr1[a] - arr2[b]))

        # Move pointer of list with smaller value (potentially make
        # difference smaller). If you move the greater value, the
        # difference is guaranteed to be greater than the previous.
        if arr1[a] < arr2[b]:
            a += 1
        else:
            b += 1
    return diff


# Check whether array is sorted recursively
def isSorted(arr,i,n):
    # Return true once i reaches len(arr)-1. This means the
    # entire array was traversed without returning False.
    if i == n:
        return True
    if arr[i] > arr[i+1]:
        return False
    return isSorted(arr,i+1,n)


# Find the sum of distinct elements in array
def sumOfDistinctElements(arr):                         # O(n)
    s, sum = set(), 0

    # If value is not in the set, add it to the sum
    for i in range(len(arr)):
        if arr[i] not in s:
            sum += arr[i]
            s.add(arr[i])
    return sum

def sumOfDistinctElements2(arr):                        # O(nlogn)
    arr.sort()
    sum = arr[0]

    # Add to the sum only if the next value is not
    # equal to the current value
    for i in range(len(arr)-1):
        if arr[i] != arr[i+1]:
            sum += arr[i+1]
    return sum


# Sort such that the first part contains odd numbers sorted in descending
# order and the rest contains even numbers sorted in ascending order
""" Does not work if there are negative numbers in input array """
def sortOddThenEven(arr):
    # Make all odd numbers negative
    for i in range(len(arr)):
        if arr[i] % 2 == 1:
            arr[i] *= -1

    arr.sort()

    # Change all odd numbers back to positive
    for i in range(len(arr)):
        if arr[i] % 2 == 1:
            arr[i] *= -1
    return arr


# Sort such that the first part contains even numbers sorted in ascending
# order and the rest contains odd numbers sorted in descending order
""" Create two temporary arrays, storing even values in the even array and
odd values in the odd array. Normal sort the even array and reverse sort the
odd array, then append the two arrays together. """


# Print three integers in sorted order without using if statements
def sortWithoutIfStatement(a,b,c):
    maxVal = max(a, max(b,c))
    minVal = min(a, min(b,c))

    midVal = (a + b + c) - (maxVal + minVal)
    temp = [minVal, midVal, maxVal]
    return temp


# Given a sorted array of positive and negative integers, sort the square of their numbers
""" Another method: Square each element (O(n)) and then sort them (O(nlogn)) time.
                        return sorted(x*x for x in arr)
    Below method:   O(n) """
def sortSquares(arr):
    res = [0 for i in range(len(arr))]
    i, j, k = 0, len(arr)-1, len(arr)-1

    while i <= j:
        # Take the absolute value of both numbers. The greater
        # value will have a greater square. Add that value to
        # the current k index of the result array.
        left, right = abs(arr[i]), abs(arr[j])
        if left > right:
            res[k] = left * left
            i += 1
        else:
            res[k] = right * right
            j -= 1
        k -= 1
    return res


# Sort an array where two halves are already sorted
def sortSortedHalves(arr):
    res = [0 for n in range(len(arr))]
    j = 0

    # Find starting index of second half
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            j = i+1
            break

    # If j remains zero, the array is already sorted
    if not j: return

    a, b, k = 0, j, 0

    # Iterate until a is less than the starting index of the
    # second half and b is less than the length of the array
    while a < j and b < len(arr):
        if arr[a] < arr[b]:
            res[k] = arr[a]
            a += 1
        else:
            res[k] = arr[b]
            b += 1
        k += 1

    while a < j:
        res[k] = arr[a]
        a += 1
        k += 1

    while b < len(arr):
        res[k] = arr[b]
        b += 1
        k += 1

    return res


# Find minimum difference between maximum and minimum of all possible k-length subsets
def findMinInSubsets(arr,k):
    # Sorting brings value-wise elements close together,
    # so there is no need to find all possible subsets
    arr.sort()
    minDiff = float('inf')

    # Sliding window approach
    for i in range((len(arr)-k)+1):
        diff = arr[i+k-1] - arr[i]      # Max - min in subset
        minDiff = min(minDiff,diff)
    return minDiff


# Given an array, the task is to remove the array elements from the series of
# natural numbers (1...n), and find the kth smallest number in the remaining set.
def kthSmallest(arr,k):
    # Increment k for every value in the array
    for i in range(len(arr)):
        k = k + 1
    return k

def kthSmallest2(arr,k):
    # Declare an arbitrary count number, say 100, in this case
    count = [0 for i in range(100)]

    # For each element in the array, change its count index to 1
    for j in range(len(arr)):
        count[arr[j]] = 1

    # Iterate, starting from 1. If the value is not in the array
    # (count=1), decrement k. When k reaches 0, return the pth index.
    for p in range(1,100):
        if count[p] != 1:
            k -= 1

        if not k:
            return p


# Find the minimum possible sum of two numbers formed by the digits of the array,
# where all digits must be used
def sumOfDigits(arr):
    arr.sort()
    a = b = 0

    for i in range(len(arr)):
       # Fill a and b with every alternate digit of input array
        if i % 2 == 0:
            a *= 10 + arr[i]
        else:
            b = b * 10 + arr[i]
    return a + b


# Given an array of distinct elements and a range, find all numbers that are
# in that range, but not in the array
def printElementsNotInRange(arr,low,high):              # O(n + (high-low+1))
    # Create a set of the array values
    s = set(arr)

    # Iterate through the range. If the value is not in
    # the set, print it.
    for i in range(low,high+1):
        if i not in s:
            print(i, end=' ')


# Find the maximum product of a triplet
def maxProductOfTriplet(arr):
    arr.sort()

    # Max product can either be the product of the three highest
    # numbers or the two lowest numbers (if negative) multiplied
    # by the highest number
    return max(arr[-1] * arr[-2] * arr[-3], arr[0] * arr[1] * arr[-1])


# Sort an almost sorted array where only two elements are swapped
def sortByOneSwap(arr):
    for i in range(len(arr)-1,-1,-1):

        # Element found when it is less than the element before it
        if arr[i] < arr[i-1]: 
            j = i-1
            while j >= 0 and arr[i] < arr[j]:
                j -= 1
            arr[i], arr[j+1] = arr[j+1], arr[i]
            break
    return arr


# Find the minimum number of subsets with consecutive numbers
def consecutiveNumberSubsets(arr):
  arr.sort()

  count = 1
  for i in range(len(arr)-1):
    # New subset exists if adjacent numbers are not consecutive
    if (arr[i] + 1 != arr[i+1]):
      count += 1
  return count


# Find maximum repeating element in an array
""" Better method: Create a hash that stores the count of each element in
                   the array, and return the maximum count - O(n).

    Below method:  O(nlogn) due to sorting """
def findMaxRepeatingElement(arr):
    cur = maxElement = arr[0]
    count = maxCount = 1

    arr.sort()      # Sort the values

    for i in range(1,len(arr)):
        # If current element does not equal to previous element,
        # set current element to cur and reset count to 1. Else,
        # increment count by 1.
        if arr[i] != cur:
            cur = arr[i]
            count = 1
        else:
            count += 1

        # Updates current count and maximum element if
        # current count is greater than maximum count
        if count > maxCount:
            maxCount = count
            maxElement = cur


# Given two arrays, determine whether there exists a pair of elements
# that sum to K in O(nlogn) time
""" Sort array1. Iterate through array2, and for each iteration, perform
binary search to check if K-arr[i] exists in array1.

Time complexity: O(nlogn) = O(nlogn) to sort and O(logn) to perform search """


# Sort zeros and ones
def sortZerosAndOnes(arr):
    res = [0 for i in range(len(arr))]

    count = 0
    # Count the number of zeros in the array
    for num in arr:
        if num == 0:
            count += 1

    # Traverse the array, starting from count (since the
    # elements in the result array are defaulted to 0),
    # and change the value to 1
    for k in range(count,len(res)):
        res[k] = 1
    return res


# Sort an array of 0's, 1's, and 2's
"""
Method 1: Use counting sort by creating a temporary array with 3 elements.

Method 2: Use quick sort, and select 1 as the pivot.
"""


squares = [-7,-3,2,3,11]
print(sortSquares(squares))
