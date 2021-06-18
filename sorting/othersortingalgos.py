# Tree sort
"""
Adds each item to a BST and then performs in-order traversal

Time complexity:
    Best case       O(nlogn)
    Average case    O(nlogn)
    Worst case      O(n^2)      (occurs when tree is skewed)

Space complexity:   O(n)

"""


# Counting sort
"""
- Assums each of the elements in in range 0 to k
- Efficient if range of input data is not significantly greater than number
  of objects to be sorted

Algorithm:
    1. Declare a count array of size k with all values defaulted to 0.
            = O(k) time and space
    2. Traverse the input array and store the count of the value in the
       count array at index "value". For example, if first element is 2,
       make count[2] = 1. If 2 is found again, increment count[2] by 1.
            = O(n) time
    3. Modify the count array so that count[i] = count[i] + count[i-1].
       The value at index k-1 in the count array will hold the length
       of the input array.
            = O(k) time
    4. Create a result array with the size of the value at index k-1 in
       count array (or simply size of the input array).
            = O(k) or O(n) time and space
    5. Traverse the input array and place the value at the index listed in
       count array, then decrease count.

Time complexity:    O(n+k)
Space complexity:   O(k)

"""


# Bogo/permutation sort
"""
Algorithm: Shuffle list, and check if sorted. If not, repeat steps.

Time complexity:
    Best case       O(n)        (already sorted)
    Average case    O((n*n)!)
    Worst case      O(inf)

"""
