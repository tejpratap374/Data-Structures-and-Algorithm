# LeetCode 99: Recover Binary Search Tree
#
# Problem: Exactly two nodes in a BST are swapped by mistake.
# Goal: Recover the BST without changing its structure.
#
# Approach:
# Use inorder traversal to detect the two misplaced nodes.
# In a valid BST, inorder traversal is strictly increasing.
# When two nodes are swapped, we find the first node where current value is less
# than previous value, and the last such violation.
#
# This is O(n) time and O(h) space (recursion stack).


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def recoverTree(root):
    prev = None
    first = None
    second = None

    def inorder(node):
        nonlocal prev, first, second

        if node is None:
            return

        inorder(node.left)

        if prev is not None and node.val < prev.val:
            if first is None:
                first = prev
            second = node

        prev = node
        inorder(node.right)

    inorder(root)

    if first is not None and second is not None:
        first.val, second.val = second.val, first.val

    return root


# Example usage
if __name__ == "__main__":
    # Example 1: [1, 3, null, null, 2]
    root = TreeNode(1)
    root.right = TreeNode(3)
    root.right.left = TreeNode(2)

    recoverTree(root)

    def inorder(node):
        if node is None:
            return
        inorder(node.left)
        print(node.val, end=" ")
        inorder(node.right)

    print("Recovered BST inorder:")
    inorder(root)
