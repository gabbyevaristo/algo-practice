# Determine if a word or list is a palindrome or not, using a stack
def palindrome(word):
    stack, i = [], 0
    mid = len(word) / 2

    # Add the first half of elements to a stack
    while i < mid:
        stack.append(word[i])
        i += 1

    # If the length is odd, add 1 to i (bypassing the middle value)
    if len(word) % 2 == 1: i += 1
    while i < len(word):
        if word[i] != stack.pop():
            return False
        i += 1

    return True


# Determine if a word or list is a palindrome or not, using two pointers
def palindromeTwoPointers(word):
    i, j = 0, len(word)-1

    # Two pointers go inwards. As long as the values are the same, i and
    # j are incremented and decremented appropriately
    while i < j:
        if word[i] != word[j]:
            return False
        i += 1
        j -= 1
    return True


# Remove all adjacent duplicates
def removeAdjacentDuplicates(word):
    ptr, i = -1, 0
    length = len(word)
    while i < length:
        if ptr == -1 or word[ptr] != word[i]:
            ptr += 1
            word[ptr] = word[i]
            i += 1
        else:
            while i < length and word[ptr] == word[i]:
                i += 1
            ptr -= 1


# Check whether each successive pair of numbers in a stack is consecutive
# or not. If stack is odd, element at the back is left out.
def pairwiseConsecutive(stack):
    # Add values to a temporary stack (first element will be on tos)
    temp = []
    while stack:
        temp.append(stack.pop())

    result = True
    while len(temp) > 1:
        x = temp.pop()
        y = temp.pop()
        if abs(x-y) != 1:           # Can just return False if function does not say
            result = False          # stack needs to retain original stack content

        stack.append(x)             # Add values back to stack
        stack.append(y)

    if len(temp) == 1: stack.append(temp.pop())
    return result


# Gets the next greatest value to the right of each index
""" This method just prints the next greatest value for each index. The values
staying in order is not guaranteed. Time complexity is O(n^2). """
def nextGreatestNaive(arr):
    for i in range(len(arr)):
        maxVal = -1
        for j in range(i+1,len(arr)):   # Searches from index+1 and onwards
            if arr[i] < arr[j]:         # Once the nearest max value is found,
                maxVal = arr[j]         # the loop breaks
                break
        print(str(arr[i]) + " --> " + str(maxVal))

""" This method performs the algorithm in O(n) time by using a stack. """
def nextGreatestOptimized(arr):
    s = []

    for i in range(len(arr)):
        # If the current value is greater than the value at the tos, pop tos
        while s and arr[i] > s[len(s)-1]:
            x = s.pop()
            print(str(x) + " --> " + str(arr[i]))
        s.append(arr[i])

    # All values still in the stack have no nearest greater element
    while s:
        print(str(s.pop()) + " --> " + str(-1))

""" This method creates an array to store the values, outputting them in order. """
def nextGreatestInOrder(arr):
    s = []
    arr1 = [0 for i in range(len(arr))]     # Create a defaulted temp array
    5, 3, 12, 4
    s = [212]
    arr1 = [0,0,-1,-1]
    for i in range(len(arr)-1,-1,-1):
        # Guarantees that the top of the stack will be the next greater
        # element on the right
        while s and s[-1] <= arr[i]:
            s.pop()

        # If the stack is empty, it means there are no elements greater to
        # it on the right
        if s:
            arr1[i] = s[-1]
        else:
            arr1[i] = -1

        s.append(arr[i])

    for i in range(len(arr)):       # Can also just return arr1
        print(str(arr[i]) + " --> " + str(arr1[i]))


# Finds the value of nearest element to the right that has frequency greater
# than that of the current element
def nextGreaterFrequencyNaive(arr):
    # Creates a dictionary and adds the frequency of each element to it
    d = {}
    for i in arr:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1

    arr1 = [0 for i in range(len(arr))]

    for i in range(len(arr)):
        cond = False
        for j in range(i+1,len(arr)):       # Searches from index and onwards
            if d[arr[j]] > d[arr[i]]:       # If frequency is greater than current
                arr1[i] = arr[j]            # frequency, set that element to the
                cond = True                 # index in the new array
                break
        if not cond:
            arr1[i] = -1

    print(arr1)

""" Optimized version of the algorithm above by using a stack. """
def nextGreaterFrequency(arr):
    d = {}
    for i in arr:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1

    s = []
    arr1 = [0 for i in range(len(arr))]
    for i in range(len(arr)-1,-1,-1):
        while s and d[s[-1]] <= d[arr[i]]:      # At the end, stack will contain
            s.pop()                             # next greater frequency element

        arr1[i] = s[-1] if s else -1    # If stack is empty (all elements popped), the
                                        # value has no greater frequency element
        s.append(arr[i])

    print(arr1)


# Find the maximum product of indexes of next greater on left and right
""" Ex.                   [5,4,9,2,8]
            L = [0,1,0,3,3]         R = [3,3,0,5,0]
              max of L*R = max([0,3,0,15,0]) = 15

Note: indexes start from 1
"""
def maxIndices(arr):
    leftS, rightS = [], []
    left = []
    right = [0 for i in range(len(arr))]

    # Can follow the same procedure as left method and then reverse the array
    for i in range(len(arr)-1,-1,-1):
        while rightS and arr[i] >= rightS[-1][0]:
            rightS.pop()
        if rightS:
            right[i] = rightS[-1][1]
        rightS.append((arr[i],i+1))

    for i in range(len(arr)):
        while leftS and arr[i] >= leftS[-1][0]:
            leftS.pop()
        if leftS:
            left.append(leftS[-1][1])
        else:
            left.append(0)
        leftS.append((arr[i],i+1))

    ans = float('-inf')
    for i in range(len(arr)):
        ans = max(ans, left[i] * right[i])

    return ans


# Given an array, delete the middle value
def deleteMiddle(arr):
    mid = len(arr) / 2
    s = []

    # The value is only added to the temporary stack if it is
    # not the middle value
    for i in range(len(arr)):
        if i != mid:
            s.append(arr[i])

    return s


# Delete middle of the array recursively
""" In the main function, print the array after the function is called. """
def deleteMiddleRecur(arr,n,cur=0):
    if cur == n or not arr:
        return

    j = arr[-1]
    arr.pop()
    deleteMiddle(arr,n,cur+1)

    if cur != n/2:
        arr.append(j)


# Reverse individual words in a given sentence
def reverseWords(sentence):
    s, reverse = [], []
    for i in range(len(sentence)):
        # Add all letters before a space to the stack
        if sentence[i] != ' ':
            s.append(sentence[i])
        else:
            # When a space is encountered, pop all items from the stack
            # and add them to the result list
            while s:
                reverse.append(s.pop())
            reverse.append(sentence[i])     # Add a space

    # Since there is no space after the last word, add it to the result list
    while s:
        reverse.append(s.pop())

    return ''.join(reverse)


# Sort a stack, using a temporary stack, in ascending order
""" To sort an array using a stack, add all the element of the array to a stack. Perform
the sort stack function below. Add all elements back to the array. """
def sortStack(arr):
    s = []

    while arr:
        val = arr.pop()

        # Adds the value back to arr if it is greater than the popped value (makes
        # room for the lesser value to be added)
        while s and s[-1] > val:
            arr.append(s.pop())
        s.append(val)
    return s


# Removes k elements that are lesser than their next element
def delete(arr,k):
    s = []
    s.append(arr[0])
    count = 0

    for i in range(1,len(arr)):
        while s and count < k and arr[i] > s[-1]:
            s.pop()
            count += 1
        s.append(arr[i])    # Once count=k, the rest of the elements are simply added

    return s


print(delete([1,2,4,6], 2))
