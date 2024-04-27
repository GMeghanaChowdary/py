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

# Function to perform reverse inorder traversal and store elements in a list
def reverse_inorder(root, elements):
    if root:
        reverse_inorder(root.right, elements)
        elements.append(root.val)
        reverse_inorder(root.left, elements)

# Function to find the kth largest element in the BST
def kth_largest(root, k):
    elements = []
    reverse_inorder(root, elements)
    return elements[k - 1]

# Main function
if __name__ == "__main__":
    n = int(input())
    elements = list(map(int, input().split()))
    k = int(input())

    root = None
    for element in elements:
        root = insert(root, element)

    kth_largest_element = kth_largest(root, k)
    print(kth_largest_element)
