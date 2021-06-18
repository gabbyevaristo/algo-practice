# Determine if a string of parenthesis () is valid or not
""" The method below uses extra space for a stack. For O(1) space, use the same
method as in finding parenthesis depth. Increment the count if an opening parenthesis
is encountered, else decrement the count. """
def isParenthesisValid(brackets):
    stack = []

    for c in brackets:
        if c == '(':
            stack.append(c)
        if not stack:
            return False
        if c == ')':
            stack.pop()

    return True if not stack else False


# Determine if a string of brackets ([{}]) is valid or not
def areBracketsValid(brackets):
    stack = []

    for c in brackets:
        # If character is an opening bracket, add it to the stack
        if c == '(' or c == '[' or c == '{':
            stack.append(c)

        # At this point, if the stack is empty, no opening bracket is detected
        if not stack:
            return False

        # Depending on the closing bracket, pop from the top of the stack and
        # compare the two characters.
        if c == ')':
            x = stack.pop()
            if x != '(':
                return False
        elif c == ']':
            x = stack.pop()
            if x != '[':
                return False
        else:
            x = stack.pop()
            if x != '{':
                return False

    # At the end of the loop, the stack should be empty. If so, return True
    return True if not stack else False


# Given an index, find the index of its closing bracket
def findClosingBracket(brackets,i):
    if brackets[i] != '(': return -1    # If character is not a (, there is no closing bracket

    s = []

    # Start from the given index. If it's an opening bracket, push it to the stack. If it's a
    # closing bracket, pop it. If the stack become empty (matching brackets), return the index.
    for k in range(i,len(brackets)):
        if brackets[k] == '(':
            s.append(brackets[i])
        elif brackets[k] == ')':
            s.pop()

        if not s:
            return k
    return -1


# Find the maximum depth of nested parenthesis in a string
def parenthesisDepth(arr):
    maxCount, count = float('-inf'), 0

    for c in arr:
        # Increment count if character is an opening bracket
        if c == "(":
            count += 1
            if count > maxCount:
                maxCount = count
        # Decrement count if character is opening bracket. If count falls below
        # 0 (too many closing brackets), return -1
        else:
            count -= 1
            if count < 0:
                return -1

    # If count does not equal 0, there are too many opening brackets
    if count != 0: return -1
    return maxCount


# Find the span for each day in the array
""" Span for a given day = max number of consecutive days before it such that the price
is less than or equal to it (includes the given day) """
def stockSpan(arr):
    # Creates a new array where each value is defaulted to 1
    span = [1 for i in range(len(arr))]
    s = [0]

    for i in range(1,len(arr)):
        # If the value on top of the stack is smaller than the current value, pop it. Subtracting
        # the next value on top of the stack from the current index will produce the span.
        while s and arr[i] >= arr[s[-1]]:
            s.pop()

        # If the stack is empty, all values before it are less than it
        span[i] = i+1 if not s else i-s[-1]
        s.append(i)
    return span


# Return the length of the longest valid substring of panrethesis
def lengthOfLongestValidSubstring(arr):
    s = [-1]            # Push -1 since index of last element-(-1) = length of entire string
    result = 0

    for i in range(len(arr)):
        if arr[i] == '(':
            s.append(i)
        else:
            s.pop()

            if s:                                   # If there are values in the stack,
                result = max(result, i - s[-1])     # current result is current index-top of stack
            else:
                s.append(i)
    return result


# Reverse a string
def reverseString(str):
    # return str[::-1] will also work without using extra space

    s = []
    for c in str:                   # Add all values to the stack
        s.append(c)

    result = ['' for i in str]      # Create a list with the same length of str

    for i in range(len(str)):       # Add the values to the result by pop
        result[i] = s.pop()
    return ''.join(result)


# Keep track of the maximum elemnent in a stack
def maxElement(arr):
    maxStack = [arr[0]]
    max = float('-inf')

    for i in range(1,len(arr)):
        # If the current value is greater than the previous maximum value, add
        # current value to the stack. Else, just add the previous maximum value
        if arr[i] > maxStack[-1]:
            maxStack.append(arr[i])
        else:
            maxStack.append(maxStack[-1])
    return maxStack


# Check if any two of the same words are consecutive, then destroy both, and return
# the number of words left in the sequence
def deleteConsecutiveWords(seq):
    s = []

    for i in range(len(seq)):
        if not s:                   # Add value to stack is stack is empty
            s.append(seq[i])
        else:
            if seq[i] == s[-1]:     # If stack exists and consecutive words are the same,
                s.pop()             # pop the value off the stack
            else:
                s.append(seq[i])
    return len(s)


print(deleteConsecutiveWords(["tom","bob","jerry","jerry","tom"]))
