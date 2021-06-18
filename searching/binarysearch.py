# Time complexity: O(logn)

def binarySearchIteratively(arr,target):
    low, high = 0, len(arr)-1

    while low <= high and target >= arr[low] and target <= arr[high]:
        mid = (low + high) / 2

        # For interpolation search:
        # mid = low + int((float(high - low) /
        #   (arr[high] - arr[low])) * (target - arr[low]))

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1

    return -1


def binarySearchRecursively(arr,target):
    return binarySearchHelper(arr,target,0,len(arr)-1)

def binarySearchHelper(arr,target,low,high):
    if low > high:
        return -1
    else:
        mid = (low + high) / 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return binarySearchHelper(arr,target,0,mid-1)
        else:
            return binarySearchHelper(arr,target,mid+1,high)



arr = [1,3,5,6,7,9,10]
print(binarySearchRecursively(arr, 9))


def search(arr):
    dom = set()
    dom.add(arr[0])
    cur_x = arr[0][0]
    cur_y = arr[0][1]

    for i in range(1,len(arr)):
        if arr[i][0] == cur_x or arr[i][1] > cur_y:
            dom.add(arr[i])
            cur_x = arr[i][0]
            cur_y = arr[i][1]
    return dom


arr = [(7,4),(7,3),(4,1),(3,2),(2,1),(1,6),(1,1),(0,0)]
print(search(arr))
