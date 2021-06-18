def createHeap():
    return []


""" Return minimum value, which is at the root of the heap """
def getMin(arr):
    return arr[0]


""" Delete minimum value, which is at the root of the heap """
def delete(arr):
    arr[0] = arr.pop()          # Replace root with last element
    root, n = 0, len(arr)       # n stores heap length after deletion

    # Heapify the root node in a top down approach
    heapifyDelete(arr,root,n)


""" Heapify the min heap after deletion using a top down approach """
def heapifyDelete(arr,i,n):
    # Store index of current node and get index of left and right child
    val = i
    left, right = 2*i + 1, 2*i + 2

    # Only changes val if children are within range and their values are
    # less than the current value
    if left < n and arr[left] < arr[val]:
        val = left
    if right < n and arr[right] < arr[val]:
        val = right

    # If val = i, the value at index i is lower than any of its two children,
    # and no swaps need to occur
    if val != i:
        arr[i], arr[val] = arr[val], arr[i]
        heapifyDelete(arr,val,n)


""" Insert into min heap """
def insert(arr,data):
    arr.append(data)        # Add element to the end of the list
    n = len(arr)

    if n == 1:              # Return if heap has only one element
        return

    # Heapify the current leaf node by sending array and node index
    heapifyInsert(arr,n-1)


""" Heapify the min heap after insertion using a bottom up approach """
def heapifyInsert(arr,i):
    parent = (i-1) / 2      # Get parent of current node

    # If parent is valid and if parent is greater than current node, swap them
    if parent >= 0 and arr[parent] > arr[i]:
        arr[i], arr[parent] = arr[parent], arr[i]
        heapifyInsert(arr,parent)


heap = createHeap()
insert(heap,3)
insert(heap,1)
insert(heap,9)
insert(heap,6)
insert(heap,12)
insert(heap,4)
insert(heap,122)
insert(heap,2)
delete(heap)
print(heap)
