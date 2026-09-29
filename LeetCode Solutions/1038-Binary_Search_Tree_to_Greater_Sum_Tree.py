# LeetCode 1038: Binary Search Tree to Greater Sum Tree
#
# Given a BST, convert each node value to the sum of all original keys
# greater than or equal to that node's original value.
#
# Idea:
# Traverse the tree in reverse inorder (right -> root -> left).
# Maintain a running sum of all values already processed.
# For each node, add the running sum to the current node and then update
# the running sum to include the node's new value.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def bstToGreaterTree(root):
    # running_sum stores the sum of all processed larger values.
    running_sum = 0

    def dfs(node):
        nonlocal running_sum

        if node is None:
            return

        # Process right subtree first so larger values are handled first.
        dfs(node.right)

        # Add the current node's original value to the running total.
        # The new value becomes original + sum of greater nodes.
        node.val += running_sum
        running_sum = node.val

        # Then process the left subtree.
        dfs(node.left)

    dfs(root)
    return root


# Example usage
if __name__ == "__main__":
    # Example tree:
    #        4
    #       / \
    #      1   6
    #     / \ / \
    #    0  2 5  7
    #      /     \  \
    #     3       8
    root = TreeNode(4)
    root.left = TreeNode(1)
    root.right = TreeNode(6)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(7)
    root.left.right.right = TreeNode(3)
    root.right.right.right = TreeNode(8)

    bstToGreaterTree(root)

    def inorder(node):
        if node is None:
            return
        inorder(node.left)
        print(node.val, end=" ")
        inorder(node.right)

    inorder(root)
