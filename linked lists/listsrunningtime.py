data = data1 = data2 = []
val, j, k, c = 1, 1, 1, 1

""" Operation              Running Time """

len(data)                  # O(1)          List instance maintains list length
data[j]                    # O(1)
data.count(val)            # O(n)          Must iterate through entire list (val could be at last index)
data.index(val)            # O(k+1)        O(n) in the worst case (val is at last index)
val in data                # O(k+1)        O(n) in the wost case (val is not in data)
data1 == data2             # O(k+1)        RT proportional to the length of the shorter list
    # (!=, <, <=, etc)
data[j:k]                  # O(k-j+1)      RT proportional to the length of the result
data1 + data2              # O(n1+n2)      ""                                       ""
c * data                   # O(cn)         ""                                       ""

data[j] = val              # O(1)          Simply replaces element without affecting any other elements
data.append(val)           # O(1)          Adds to the back
data.insert(k,val)         # O(n-k+1)      RT proportional to number of elements being shifted
data.pop()                 # O(1)          Removes from the back
data.pop(k)                # O(n-k)        RT proportional to number of elements being shifted
del data[k]                # O(n-k)        ""                                               ""
data.remove(val)           # O(n)          Only O(n) in worst case (val not in list or val is at last index)
data1.extend(data2)        # O(n2)         RT proportional to the length of the second list
""" Appending one list to another. Better than using append as there is less overhead
        to a single function call """
data1 += data2             # O(n2)
data.reverse               # O(n)
data.sort()                # O(nlogn)



# List comprehension
""" The first method is better as multiple append calls can get expensive for large input """

squares = [[k*k] for k in range(1,j+1)]         # Method 1

squares = []                                    # Method 2
for k in range(1,j+1):
    squares.append(k*k)



# Strings

""" DO NOT USE += ON STRINGS. For each letter c, a new letters string is being created = O(n^2) """
letters = ''                                                # Method 1
for c in squares:
    if c.isalpha():
        letters += c

""" Improves on Method 1. Only O(n) as there are n calls to append """
temp = []                                                   # Method 2
for c in squares:
    if c.isalpha():
        temp.append(c)
letters = ''.join(temp)

""" Uses a temporary list for list comprehension """
letters = ''.join([c for c in squares if c.isalpha()])      # Method 3

""" Better than all methods. Does not use a temporary list as Method 3 does """
letters = ''.join(c for c in squares if c.isalpha())        # Method 4
