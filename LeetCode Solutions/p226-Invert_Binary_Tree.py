from collections import deque

# Tree node with left and right child pointers.
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


# Invert a binary tree by swapping left and right children recursively.
def invertTree(root):
    # Base case: empty tree
    if root is None:
        return

    # Recurse on both subtrees.
    left = invertTree(root.left)
    right = invertTree(root.right)

    # Swap the children of the current node.
    root.left = right
    root.right = left

    return root


# Print nodes level by level from left to right.
def levelOrder(node):
    if node is None:
        return

    queue = deque()
    queue.append(node)

    while queue:
        current = queue.popleft()
        print(current.data, end=" ")

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)


if __name__ == "__main__":
    # Build a sample binary tree.
    nodeA = TreeNode('A')
    nodeB = TreeNode('B')
    nodeC = TreeNode('C')
    nodeD = TreeNode('D')
    nodeE = TreeNode('E')
    nodeF = TreeNode('F')
    nodeG = TreeNode('G')

    nodeA.left = nodeB
    nodeA.right = nodeC
    nodeB.left = nodeD
    nodeB.right = nodeE
    nodeC.left = nodeF
    nodeC.right = nodeG

    # Print original level order.
    levelOrder(nodeA)

    # Invert the tree.
    invertTree(nodeA)
    print()

    # Print inverted level order.
    levelOrder(nodeA)
    