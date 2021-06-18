# Find maximum depth given multiple trees in parent array form
""" Best if multiple trees (multiple values have -1) exist """
def findMaxDepth(arr):
    depth, maxDepth = {}, float('-inf')

    # Perform search (BFS) on each spcecies with no predator
    for i in range(len(arr)):
        if arr[i] == -1:
            depth[i] = 1         # If node exists, then depth = 1
            fillDepth(arr, i, depth)

    # Find the maximum depth and return it
    for i in range(len(arr)):
        if depth[i] > maxDepth:
            maxDepth = depth[i]

    return maxDepth


def fillDepth(arr,i,depth):
    # Create a queue and append predator to it
    q = [i]

    while q:
        val = q.pop(0)
        for i in range(len(arr)):
            if arr[i] == val:                # If value is a child of current node,
                q.append(i)                  # then append it to the queue
                depth[i] = depth[val] + 1    # In this instance, j = child and val = parent



# Find maximum depth given a tree in parent array form
def findMaxDepth1(arr):
    # Creates a depth array to store depth of all nodes
    depth = [0 for i in range(len(arr))]

    # Fill depth of all nodes
    for i in range(len(arr)):
        fillDepth1(arr,i,depth)

    maxDepth = float('-inf')
    for i in depth:
        maxDepth = max(maxDepth,i)

    return maxDepth


def fillDepth1(arr,i,depth):
    # Return if node is already filled
    if depth[i] != 0:
        return

    # Declare root to have depth of 1
    if arr[i] == -1:
        depth[i] = 1
        return

    # If node has a parent and node's parent's depth is not filled,
    # fill it. When reversing backwards, the depth of each node will
    # be filled.
    if depth[arr[i]] == 0:
        fillDepth1(arr,arr[i],depth)

    # Depth of node = depth of parent node + 1
    depth[i] = depth[arr[i]] + 1


def printTree(arr):
    d, children = {}, set()
    for i in range(len(arr)):
        if arr[i][0] not in d:
            d[arr[i][0]] = []
        d[arr[i][0]].append(arr[i][1])
        children.add(arr[i][1])

    parent = None
    for val in d:
        if val not in children:
            parent = val

    dfs(parent, d, 0)

def dfs(parent, d, depth):
    res = ""
    for i in range(depth):
        res += "\t"
    res += parent
    print(res)

    if parent in d:
        children = d[parent]
    else:
        return

    for child in children:
        dfs(child, d, depth + 1)



tree = [("animal", "mammal"), ("animal", "bird"), ("lifeform", "animal"), ("cat", "lion"), ("mammal", "cat"), ("animal", "fish")]
print(printTree(tree))
