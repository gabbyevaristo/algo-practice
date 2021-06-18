# Find only repeating element in array
"""
1. Sort, traverse the array, and return arr[i] if arr[i] = arr[i+1].
2. Traverse the array forwards, adding each element to a hash. Once
   we see a value already in the hash, return that value.
"""


# Find the first repeating element in an array
def findFirstRepeating(arr):
    d = {}

    # Store the negative index + 1 for each value (1 is added to account
    # for index 0 since it cannot be negated). If we see the value a
    # second time, make the index positive (so only values with positive
    # indices have been repeated).
    for i in range(len(arr)):
        if arr[i] in d:
            d[arr[i]] = abs(d[arr[i]])
        if arr[i] not in d:
            d[arr[i]] = -(i+1)

    index = val = float('inf')

    # Return the value with the lowest positive index
    for num in d:
        if d[num] < index and d[num] > 0:
            val, index = num, d[num]
    return val

def findFirstRepeating2(arr):
    d, min = {}, float('inf')

    # Since we iterate backwards, the last repeated element
    # we see will be set to min
    for i in range(len(arr)-1,-1,-1):
        if arr[i] in d:
            min = arr[i]
        if arr[i] not in d:
            d[arr[i]] = 1
    return min


# Find all common elements given three arrays
def findCommonElements(arr1,arr2,arr3):                 # O(n1 + n2 +n3)
    i = j = k = 0

    # Stop when one array is fully traversed
    while i < len(arr1) and j < len(arr2) and k < len(arr3):
        if arr1[i] == arr2[j] == arr3[k]:
            print(arr1[i], end=" ")
            i += 1
            j += 1
            k += 1

        # Attempt to move smaller value
        elif arr1[i] < arr2[j]:
            i += 1
        elif arr2[j] < arr3[k]:
            j += 1
        else:
            k += 1


# Find a pair of numbers that sum to a given target
""" Another method: Sort and then perform two pointer approach - O(nlogn) """
def findPairSum(arr,target):                        # O(n)
    s = set()

    for i in range(len(arr)):
        if target - arr[i] in s:
            return (arr[i],target-arr[i])

        s.add(arr[i])
    return -1


# Find a pair of numbers with the given target difference
def findPairDifference(arr,target):
    s = set()

    # Pair exists if either target + arr[i] or
    # arr[i] - target is in the set
    for i in range(len(arr)):
        if target + arr[i] in s:
            return (arr[i],arr[i]+target)
        elif arr[i] - target in s:
            return (arr[i],arr[i]-target)

        s.add(arr[i])
    return -1


# Find triplets in an array that sum to 0
""" Performs hashing in the inner loop """
def findTriplets(arr):                              # O(n^2)
    found = False

    for i in range(len(arr)-1):
        # For each iteration, create a set
        s = set()
        for j in range(i+1,len(arr)):
            # Print pair if x is in the set
            x = -(arr[i] + arr[j])
            if x in s:
                print(x, arr[i], arr[j])
                found = True
            else:
                s.add(arr[j])

    if not found: return "No triplet found"

""" Sorts the array and then performs two pointer approach in the inner loop """
def findTriplets2(arr):                              # O(n^2)
    arr.sort()

    for i in range(len(arr)-2):
        j, k = i+1, len(arr)-1

        while j < k:
            # Pair exists if two values sum to the
            # negative of the current value
            if arr[j] + arr[k] == -arr[i]:
                print(arr[i],arr[j],arr[k])

            if arr[j] + arr[k] < -arr[i]:
                j += 1
            else:
                k -= 1


# Given a SORTED array and a value x, find a pair with sum closest to x
""" Same method to find pair with sum closest to zero """
def sumClosestToTarget(arr,x):
    a = b = 0                   # Holds pair
    i, j = 0, len(arr)-1
    diff = float('inf')

    while i < j:
        # Return directly if two values sum to x
        if arr[i] + arr[j] == x:
            return (arr[i],arr[j])

        # Store pair if their difference is less than old difference
        if abs(x - (arr[i] + arr[j])) < diff:
            diff = abs(x - (arr[i] + arr[j]))
            a, b = arr[i], arr[j]

        # If sum is greater than x, decrement j. Else, increment i.
        if arr[i] + arr[j] > x:
            j -= 1
        else:
            i += 1
    return (a,b)


# Count pairs from two arrays that sum to x. In the case of duplicate elements,
# an element can only participate in one pair.
def countPairs(arr1,arr2,x):
    d, count = {}, 0

    # Store the count of each value in array1 in a dictionary
    for i in range(len(arr1)):
        if arr1[i] not in d:
            d[arr1[i]] = 1
        else:
            d[arr1[i]] += 1

    # Iterate through array2. If pair exists in array1, increment
    # count and decrease element's dictionary value by 1.
    for i in range(len(arr2)):
        if x - arr2[i] in d and d[x-arr2[i]] != 0:      # Only increment count if
            count += 1                                  # value does not equal to 0.
            d[x-arr2[i]] -= 1
    return count


# Check if an element occurs more than n/2 times
"""
Find median, then traverse and count the number of occurences of it. If
count is greater than n/2, return the median. Else, the element does not
exist (if an element occurs more than n/2 times, it must be the median).
"""


# Find the maximum A[j] - A[i] such that j > i
def maxDifference(arr):
    maxVal, diff = arr[-1], float('-inf')

    # Traverse the array backwards, starting from the second
    # to last element, and keep track of the maximum value
    for i in range(len(arr)-1,-1,-1):
        # Update difference and maximum value if necessary
        diff = max(diff, maxVal - arr[i])
        maxVal = max(maxVal, arr[i])
    return diff


# Find first and second smallest element in array
def firstAndSecondSmallest(arr):
    min1 = min2 = float('inf')

    for i in range(len(arr)):
        if arr[i] < min1:
            min2 = min1
            min1 = arr[i]

        # Must have second condition to ensure duplicates
        # are not counted
        elif arr[i] < min2 and arr[i] != min1:
            min2 = arr[i]
    return (min1,min2)


# Find third largest in an array (duplicates only counted as 1)
def thirdLargest(arr):
    if len(arr) < 3: return

    first = arr[0]
    second = third = float('-inf')

    """ Must check if element is greater than first before checking
    if it is greater than second and third. """
    for i in range(1,len(arr)):

        # If current element is greater than first, update
        # first, second and third
        if arr[i] > first:
            third = second
            second = first
            first = arr[i]

        # If current element is between first and second
        elif arr[i] > second and arr[i] != first:
            third = second
            second = arr[i]

        # If current element is between second and third
        elif arr[i] > third and arr[i] != first and arr[i] != second:
            third = arr[i]
    return third


# Find number occuring odd number of times, when all other elements occur an even
# number of times
def findOddOccurrence(arr):
    odd = arr[0]

    # (x ^ x = 0) and (x ^ 0 = x) - since all, but one element
    # occur even number of times, their values will cancel out
    for i in range(1,len(arr)):
        odd ^= arr[i]
    return odd
