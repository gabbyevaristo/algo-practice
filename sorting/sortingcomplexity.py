# Time complexities of algorithms
"""
                Best case       Average case        Wosrt Case      Space       Stable

Bubble             O(n)            O(n^2)             O(n^2)         O(1)         Y
Selection         O(n^2)           O(n^2)             O(n^2)         O(1)         N
Insertion          O(n)            O(n^2)             O(n^2)         O(1)         Y
Shell            O(nlogn)       O((nlogn)^2)       O((nlogn)^2)      O(1)         N
Merge            O(nlogn)         O(nlogn)           O(nlogn)        O(n)         Y
Heap             O(nlogn)         O(nlogn)           O(nlogn)        O(1)         N
Quick            O(nlogn)         O(nlogn)            O(n^2)         O(1)         N
Tree             O(nlogn)         O(nlogn)            O(n^2)         O(n)         Y

"""


# Stability: A sorting algorithm is said to be stable if two objects with equal keys appear
# in the same order in the sorted output as they appear in the input array to be sorted.
"""
Mainly important when there exists key-value pairs with duplicate keys

Note: For the following examples, assume A[i] and A[j] have equal keys, where i < j

* Stable algorithms: bubble, insertion, merge, counting

    - Bubble:    Elements change order only when a smaller record follows a larger one
                 (A[i] > A[i+1], where i+1=j). Since A[i] is not greater than A[j], it
                 remains before it in the output array.
    - Insertion: Only values smaller than A[i] are shifted before it since the condition is
                 key < A[i], where key = A[j]. A[j] is not less than A[i], so it remains
                 after it in the output array.
    - Merge:     Keys in left subarray gets preference.


* Unstable algorithms: selection, heap, quick

    - Selection: The minimum element to be swapped with A[i] can occur after A[j]. When
                 swapped, A[j] will come before A[i].
    - Heap:      Say, A[i] and A[j] are the maximum value. Since A[i] comes first, it will
                 be placed at the root. When sorting, A[i] will be placed at index n-1 while
                 A[j] will be placed at index n-2.

"""


# Merge sort vs. quick sort
"""
                        Merge                       Quick
Space              Uses extra space         Requires little space

Locality of       Bad cache locality         Good cache locality
reference

Worst cases            O(nlogn)          O(n^2) but can be avoided using
                                             randomized quick sort

Preferable data  Better for large data       Better for small data

Stability                Yes                         No

Sorting method         External                    Internal

LL vs array       Preferred for LL            Preferred for arrays


    * The reason quick sort performs poorly on LL is due to the slow
      random access of LL

"""
