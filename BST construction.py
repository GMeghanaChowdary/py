class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return TreeNode(key)
    else:
        if root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.val, end=" ")
        inorder_traversal(root.right)

def construct_bst(arr):
    root = None
    for num in arr:
        root = insert(root, num)
    return root

# Input
n = int(input())
arr = list(map(int, input().split()))

# Constructing BST
root = construct_bst(arr)

# Inorder Traversal
inorder_traversal(root)
