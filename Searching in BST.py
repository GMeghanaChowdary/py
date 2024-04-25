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

def search(root, key):
    if root is None or root.val == key:
        return root is not None
    if root.val < key:
        return search(root.right, key)
    return search(root.left, key)

def construct_bst(arr):
    root = None
    for num in arr:
        root = insert(root, num)
    return root

# Input
n = int(input())
arr = list(map(int, input().split()))
target = int(input())

# Constructing BST
root = construct_bst(arr)

# Searching for target element
if search(root, target):
    print("Target element is found")
else:
    print("Target element is not found")
