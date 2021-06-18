# Time complexity: O(log[base 3]n)

def ternarySearchIteratively(arr,target):
    low, high = 0, len(arr)-1

    while low <= high and target >= arr[low] and target <= arr[high]:
        # Find mid1 and mid2
        mid1 = low + ((high - low) / 3)
        mid2 = high - ((high - low) / 3)

        # Check if target is present at any mid
        if (arr[mid1] == target):
            return mid1
        if (arr[mid2] == target):
            return mid2

        # Key lies between low and mid1
        if target < arr[mid1]:
            high = mid1-1

        # Key lies between mid2 and high
        elif target > arr[mid2]:
            low = mid2+1

        # Key lies between mid1 and mid2
        else:
            low = mid1+1
            high = mid2-1

    return -1


def ternarySearchRecursively(arr,target):
    return ternarySearchHelper(arr,target,0,len(arr)-1)

def ternarySearchHelper(arr,target,low,high):
    if low > high:
        return -1

    else:
        # Find mid1 and mid2
        mid1 = low + ((high - low) / 3)
        mid2 = high - ((high - low) / 3)

        # Check if target is present at any mid
        if (arr[mid1] == target):
            return mid1
        if (arr[mid2] == target):
            return mid2

        # Key lies between low and mid1
        if (target < arr[mid1]):
            return ternarySearchHelper(arr,target,low,mid1-1)

        # Key lies between mid2 and high
        elif (target > arr[mid2]):
            return ternarySearchHelper(arr,target,mid2+1,high)

        # Key lies between mid1 and mid2
        else:
            return ternarySearchHelper(arr,target,mid1+1,mid2-1)


arr = [1,3,5,6,7,9,10]
print(ternarySearchIteratively(arr,0))
