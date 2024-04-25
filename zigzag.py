#level order traversal
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def printzigzagOrder(root):
    result =[]
    Q = [root]
    level=0

    while len(Q) > 0:
        n = len(Q)
        subResult =[]
        for i in range(n):
            # step-1: popping
            curr = Q.pop(0)
            subResult.append(curr.data)

            # step-2: pushing left child if its not none
            if curr.left != None:
                Q.append(curr.left)

            # step-3: pushing right child if its not none
            if curr.right != None:
                Q.append(curr.right)
        if level%2==1:
            subResult=subResult[::-1]
        result.append(subResult)
        level+=1
    for i in range(len(result)):
        print(*result[i])
 #print()

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


printzigzagOrder(root)
