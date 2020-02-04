# Maximum depth of binary tree is how far you can go with a DFS.
# Assume you get only the root node, no other information about the tree.
# Note: if you're working iteratively, you know the answer at every step and are accumulating values between calls.
# Consider the space complexity of recursion instead - calls will beget multiple other calls instead of being linear,
# and you need to keep track of the calls made because only when you reach a base case do you start getting answers.

class TreeNode:
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None

def maxDepth(root: TreeNode) -> int:
    if not root:
        return 0
    # max depth must be the max depth of either the right subtree or the left subtree.
    # now we recurse.
    return 1 + max(maxDepth(root.left), maxDepth(root.right))

node_a = TreeNode('a')
node_b = TreeNode('b')
node_c = TreeNode('c')
node_d = TreeNode('d')
node_e = TreeNode('e')

node_a.left = node_b
node_a.right = node_c
node_c.left = node_d
node_c.right = node_e

print(maxDepth(node_a))