# Methods
"""
- get(k)       : returns M[k] if key k exists
- del M[k]     : removes item with key k
- pop(k)       : removes item with key k and returns associated value, v
- keys         : returns a set-like view of all keys
- values       : returns a set-like view of all values
- items        : returns a set-like view of (k,v) tuples for all entries
- clear        : removes all key-value pairs
- popitem      : removes an arbitrary key-value pair
"""

#hash table, hash function, hash code

def removeDuplicates(nums):
        n = 0
        while(n < len(nums)):
            if(nums[n]==nums[n-1]): del nums[n]
            else: n += 1
        return nums

nums = [1,4,5,5]
print(removeDuplicates(nums))

arr = [1,1,4,3,4,1,2,4,3]
d = {}
for i in arr:
    if i not in d:
        d[i] = 1
    else:
        d[i] = d[i] + 1


print(sorted(d,key=d.get,reverse=True))
