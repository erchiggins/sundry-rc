class TreeNode(object):
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

# no duplicates, and assuming that root exists


def addNode(root, value):
    # new node will go to the left of the root
    if root.value > value:
        if root.left is not None:
            # recursive case: root has left child
            addNode(root.left, value)
        else:
            # base case: root is a leaf, add new node as its left child
            root.left = TreeNode(value)
    # new node will go to the right of the root
    if root.value < value:
        if root.right is not None:
            # recursive case: root has right child
            addNode(root.right, value)
        else:
            # base case: root is a leaf, add new node as its right child
            root.right = TreeNode(value)
    # do nothing for a duplicate value

def inOrderTraverse(node):
    if node:
        inOrderTraverse(node.left)
        print(node.value)
        inOrderTraverse(node.right)

def preOrderTraverse(node):
    if node:
        print(node.value)
        preOrderTraverse(node.left)
        preOrderTraverse(node.right)

def postOrderTraverse(node):
    if node:
        postOrderTraverse(node.left)
        postOrderTraverse(node.right)
        print(node.value)

root = TreeNode(20)

addNode(root, 40)
addNode(root, 35)
addNode(root, 12)
addNode(root, 1)
addNode(root, 15)
addNode(root, 90)
addNode(root, 9)

print('in-order traversal:')
inOrderTraverse(root)

print('pre-order traversal:')
preOrderTraverse(root)

print('post-order traversal:')
postOrderTraverse(root)