# Define the Node class for the Binary Search Tree
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# Function to insert a new node with the given key
def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

# Function to perform inorder traversal and store elements in a list
def inorder(root, elements):
    if root:
        inorder(root.left, elements)
        elements.append(root.val)
        inorder(root.right, elements)

# Function to find the kth smallest element in the BST
def kth_smallest(root, k):
    elements = []
    inorder(root, elements)
    return elements[k - 1]

# Main function
if __name__ == "__main__":
    n = int(input())
    elements = list(map(int, input().split()))
    k = int(input())

    root = None
    for element in elements:
        root = insert(root, element)

    kth_smallest_element = kth_smallest(root, k)
    print(kth_smallest_element)
