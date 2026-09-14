from collections import deque

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def preOrder(node):
    if node is None:
        return
    print(node.key, end=" ")
    preOrder(node.left)
    preOrder(node.right)

def inOrder(node):
    if node is None:
        return
    inOrder(node.left)
    print(node.key, end=" ")
    inOrder(node.right)

def postOrder(node):
    if node is None:
        return
    postOrder(node.left)
    postOrder(node.right)
    print(node.key, end=" ")

def levelOrder(node):
    if node is None:
        return

    queue = deque()
    queue.append(node)
    while queue:
        current = queue.popleft()
        print(current.key, end=" ")
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

def findHeight(node):
    if node is None:
        return -1
    return max(findHeight(node.left), findHeight(node.right)) + 1

def mirrorTree(node):
    if node is None:
        return 

    queue = deque()
    queue.append(node)
    while queue:
        current = queue.popleft()
        current.left, current.right = current.right, current.left
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    
def search(node, key):
    if node is None:
        return
    
    queue = deque()
    queue.append(node)
    while queue:
        current = queue.popleft()
        if current.key == key:
            return True
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

# Helper function to delete the deepest and rightmost node
def deleteDeepest(root, d_node):
    queue = deque([root])
    while queue:
        current = queue.popleft()
        
        if current == d_node:
            root = None
            return
        
        # Check right child first since we want to clear the reference
        if current.right:
            if current.right == d_node:
                current.right = None
                return
            else:
                queue.append(current.right)

        if current.left:
            if current.left == d_node:
                current.left = None
                return
            else:
                queue.append(current.left)

# Delete FUnction
def delete(root, target):
    if not root:
        return None
    
    if root.left is None and root.right is None:
        if root.key == target:
            return None
        else:
            return root
    
    keyNode = None
    queue = deque([root])
    current = None

    # Level Order traversal to find the target node
    while queue:
        current = queue.popleft()
        if current.key == target:
            keyNode = current

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

    # If the target node is found in the tree, 
    # then overwrite the target data with the deepest rightmost nodee's data 
    if keyNode:
        x = current.key
        deleteDeepest(root, current)
        keyNode.key = x

    return root 


# root = TreeNode('R')
nodeA = TreeNode('A')
nodeB = TreeNode('B')
nodeC = TreeNode('C')
nodeD = TreeNode('D')
nodeE = TreeNode('E')
nodeF = TreeNode('F')
nodeG = TreeNode('G')

# root.left = nodeA
# root.right = nodeB
nodeA.left = nodeB
nodeA.right = nodeC
nodeB.left = nodeD
nodeB.right = nodeE
nodeC.left = nodeF
nodeC.right = nodeG
nodeC.left.left = TreeNode(7)
nodeC.left.left.right = TreeNode(4)

# print("root.right.left.key: ", root.left.left.key)

preOrder(nodeA)
print()
inOrder(nodeA)
print()
postOrder(nodeA)
print()
levelOrder(nodeA)
print()
print(findHeight(nodeA))
mirrorTree(nodeA)
levelOrder(nodeA)
print()
print("Exists" if search(nodeA, 'F') == True else "Does not exists")
root = delete(nodeA, 7)
inOrder(nodeA)
