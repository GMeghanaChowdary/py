#top view
class TreeNode:
    def __init__(self, data):
        self.data = data 
        self.left = None 
        self.right = None 




def printTopViewOfBinaryTree(root):
    result = []

    Q = [[root, 0]]
    # Q = [[12, -1], [10, 3], [14, 2], [56, 10]]
    store = dict()
    while len(Q) > 0:
        currPair = Q.pop(0)
        # [address, hd]
        node = currPair[0]
        hd = currPair[1]

        # something to insert into our result
        if hd not in store:
            store[hd] = node.data

        if node.left != None:
            Q.append([node.left, hd - 1])

        if node.right != None:
            Q.append([node.right, hd + 1])

    # key: value
    # {0: 18, -1: 15, 1: 20, -2: 25, 2: 80}
    # allKeys = [0, -1, 1, -2, 2]
    # allKeys = [-2, -1, 0, 1, 2]
    # Top view of binary-tree is:
    # []
    # print(store)
    allKeys = sorted(store.keys())
    for eachKey in allKeys:
        result.append(store[eachKey])

    #print("Top view of binary-tree is:")
    #print(result)

    for i in range(len(result)):
        print(result[i],end=" ")
    
root = TreeNode(11)
# root:
# data = 15
# left = None
# right = None
obj2 = TreeNode(7)
obj3 = TreeNode(15)
obj4 = TreeNode(5)
obj5 = TreeNode(9)
obj6 = TreeNode(13)
obj7 = TreeNode(20)
obj8 = TreeNode(3)
obj9 = TreeNode(8)
obj10 = TreeNode(10)
obj11= TreeNode(12)
obj12 = TreeNode(14)
obj13 = TreeNode(18)
obj14 = TreeNode(25)


#    18
#   15  20
# 25 30 45 80


# 2- establishing links between nodes
root.left=obj2
root.right=obj3

obj2.left=obj4
obj2.right=obj5

obj3.left=obj6
obj3.right=obj7

obj4.left=obj8

obj5.left=obj9
obj5.right=obj10

obj6.left=obj11
obj6.right=obj12

obj7.left=obj13
obj7.right=obj14

printTopViewOfBinaryTree(root)


#Bottom view
class TreeNode:
    def __init__(self, data):
        self.data = data 
        self.left = None 
        self.right = None 




def printBottomViewOfBinaryTree(root):
    result = []

    Q = [[root, 0]]
    # Q = [[12, -1], [10, 3], [14, 2], [56, 10]]
    store = dict()
    while len(Q) > 0:
        currPair = Q.pop(0)
        # [address, hd]
        node = currPair[0]
        hd = currPair[1]

        # something to insert into our result
        #if hd not in store:
        store[hd] = node.data

        if node.left != None:
            Q.append([node.left, hd - 1])

        if node.right != None:
            Q.append([node.right, hd + 1])

    # key: value
    # {0: 18, -1: 15, 1: 20, -2: 25, 2: 80}
    # allKeys = [0, -1, 1, -2, 2]
    # allKeys = [-2, -1, 0, 1, 2]
    # Top view of binary-tree is:
    # []
    # print(store)
    allKeys = sorted(store.keys())
    for eachKey in allKeys:
        result.append(store[eachKey])

    #print("Top view of binary-tree is:")
    #print(result)

    for i in range(len(result)):
        print(result[i],end=" ")
    
root = TreeNode(11)
# root:
# data = 15
# left = None
# right = None
obj2 = TreeNode(7)
obj3 = TreeNode(15)
obj4 = TreeNode(5)
obj5 = TreeNode(9)
obj6 = TreeNode(13)
obj7 = TreeNode(20)
obj8 = TreeNode(3)
obj9 = TreeNode(8)
obj10 = TreeNode(10)
obj11= TreeNode(12)
obj12 = TreeNode(14)
obj13 = TreeNode(18)
obj14 = TreeNode(25)


#    18
#   15  20
# 25 30 45 80


# 2- establishing links between nodes
root.left=obj2
root.right=obj3

obj2.left=obj4
obj2.right=obj5

obj3.left=obj6
obj3.right=obj7

obj4.left=obj8

obj5.left=obj9
obj5.right=obj10

obj6.left=obj11
obj6.right=obj12

obj7.left=obj13
obj7.right=obj14

printBottomViewOfBinaryTree(root)
