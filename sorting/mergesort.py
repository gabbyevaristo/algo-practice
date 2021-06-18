# Description
"""
- Splits list into two and then joins them back together
- Divide and conquer algorithm
- Stable

Time complexity:    O(nlogn) in all cases

Space complexity:   O(n)

"""


def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) / 2
        L = arr[:mid]       # Divide list into two halves
        R = arr[mid:]

        mergeSort(L)        # Sort the first half
        mergeSort(R)        # Sort the second half

        i = j = k = 0

        # Finds the smaller value between the two lists and inserts
        # it into the array at the correct index. The index of the
        # list taken is then incremented.
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i+=1
            else:
                arr[k] = R[j]
                j+=1
            k+=1

        # Checks if any elements were left
        while i < len(L):
            arr[k] = L[i]
            i+=1
            k+=1

        while j < len(R):
            arr[k] = R[j]
            j+=1
            k+=1


arr = [32,1,21,6,3]
mergeSort(arr,0,len(arr)-1)
print(arr)
