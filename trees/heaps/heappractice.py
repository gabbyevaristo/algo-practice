# Find maximum element in a min heap
"""
Naive method: Can search every element in O(n) time as min heaps are implemented
as arrays. Instead, we can observe that the maximum element has to be a leaf node.
Though still O(n), the time complexity factor is reduced by 1/2.
"""
def findMax(heap):
    # Leaves start from floor(n/2) and exist till end
    ceil = len(heap) / 2
    maxElement = heap[ceil]

    for i in range(ceil+1, len(heap)):        # Iterate through the leaves
        maxElement = max(maxElement, heap[i])
    return maxElement


# Delete the element at the given index
"""
Another method: First, search for the element, grab its index and run the
function below.
"""
def deleteAtIndex(arr,index):
    arr[index] = arr.pop()          # Move last element to index

    # Heapify the index node in a top down approach. There is no need to
    # start at the root as the heap is already built appropriately.
    heapify(arr,index,len(arr))


# Print all elements less than k in a min heap
""" Can use similar method to print elements greater than k in max heap """
def lessThanKInMin(arr,k,pos=0):
    # Return if position is invalid or if element is greater than k
    if pos >= len(arr) or arr[pos] >= k:
        return

    print(arr[pos])
    lessThanKInMin(arr, k, 2*pos+1)    # Traverse left child
    lessThanKInMin(arr, k, 2*pos+2)    # Traverse right child


# Print all elements less than k in a max heap
""" Can use similar method to print elements greater than k in min heap """
def lessThanKInMax(arr,k,pos=0):
    if pos >= len(arr):                # Return if position is invalid
        return

    lessThanKInMax(arr, k, 2*pos+1)    # Traverse left child
    lessThanKInMax(arr, k, 2*pos+2)    # Traverse right child

    if arr[pos] < k:                   # Print element if it is less than k
        print(arr[pos])


# Merge two max heaps
""" Append the second heap to the first heap and heapify the new heap using
heap sort = O(m+n).

How to append two arrays/lists:
    1.   heap1.extend(heap2)
    2.   for i in range(len(heap2)):
            heap1.append(heap2[i])
"""


# Find kth smallest element in min heap
"""
1. Sort the list in ascending order and return the element at the kth
   index
        O(nlogn):   nlogn to sort and 1 to get the element

2. Perform deletion on a min heap k-1 times. Inside the for loop, pop
   the last element and move the data to the root, and then heapify. At
   the end of the loop, the root will hold the kth smallest value.
        O((k-1)logn)

3. Use an auxiliary heap, say temp and default a count to 1. Starting
   with the root, add the node to temp and heapify. If count is equal to k,
   return arr[0]. Else, remove the root from temp, increment count by 1,
   and add its right and left child to temp. This is useful if k is small
   in comparison to n.
        O(klogk)

To print k smallest elements, use method 2, but instead run the loop k
times, printing arr[0] at the beginning of the loop.
"""


# Given a big file containing billions of numbers, how can you find the 10
# maximum numbers from that file?
"""
1. Divide the data set in sets of 1000 elements and create various heaps. One
   by one, take 10 elements from each heap. Then, create a heap of all elements
   taken and perform heap sort. Then take the maximum 10 elements from those.

2. Make one block of 1000 elements and the rest of 990 elements. Heap sort the
   first block and take the maximum 10 elements. Then, mix them with the 990
   elements of the second set (now 1000 elements). Repeat until the last set of
   990 (or less) elements and take the maximum 10 elements from it.
"""


# Sort a k sorted array
""" Constuct a min heap of size k+1 and push the first k+1 elements into the
heap. Remove the min value from the heap, assign it to the next available array
index, and insert the next element from the array into the heap. Continue
until both the array and heap are exhausted. Once the loop is over, pop the rest
of the elements in the heap and add them to the array.

This process uses the fact that the array is k sorted by having k elements in
the heap instead of having all n elements.
"""


# Check if a given binary tree is a min heap
def isHeap(node):
    # Size of node = number of nodes in entire tree
    return isHeapHelper(node,0,size(node))

def isHeapHelper(node,i,n):
    if not node:
        return True

    # Fails complete tree property if index is greater than size of tree or right child exists
    # and not the left
    if i > n or node.right and not node.left:
        return False

    # Fails min heap property if children data are less than node's data
    if node.left and node.left.data <= node.data \
        or node.right and node.right.data <= node.data:
        return False

    # Recur for the node's left and right child
    return isHeapHelper(node.left, 2*i+1, n) and isHeapHelper(node.right, 2*i+2, n)


# Check if a given array represents a max heap
def isHeap2(arr,i,n):
    # Return true for a leaf
    if (2*i + 2) > n:
        return True

    return arr[i] >= arr[2*i+1] and arr[i] >= arr[2*i+2] and \
        isHeap2(arr, 2*i+1, n) and isHeap2(arr, 2*i+2, n)


# Connect n ropes with minimum cost. The cost to connect two ropes is equal to the sum
# of their lengths.
from heapq import heappop, heappush, heapify

def minCost(arr,n):
    cost = 0
    heapify(arr)        # Heapify the array
    while len(arr) > 1:
        # Extract the first and second min values and add them to the cost
        firstMin, secondMin = heappop(arr), heappop(arr)
        cost += firstMin + secondMin

        # Add the cost to the heap
        heappush(arr, firstMin + secondMin)

    return cost


# Find height of a complete binary tree from given n nodes
import math

def getHeight(n):
    return math.ceil(math.log2(n+1)) - 1
