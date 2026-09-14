from collections import deque

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

# Helper Function to get the node's height
def getHeight(node):
    if node is None:
        return 0
    return node.height

# Helper function to get the balance factor of nodes
def getBalance(root):
    if not root:
        return
    return getHeight(root.left) - getHeight(root.right)

# Helper function to rotate the tree left at a given node
def leftRotate(x):
    y = x.right
    t2 = y.left
    y.left = x
    x.right = t2
    x.height = max(getHeight(x.left), getHeight(x.right)) + 1
    y.height = max(getHeight(y.left), getHeight(y.right)) + 1
    return y

# Helper function to rotate the tree right at a given node
def rightRotate(y):
    x = y.left
    t2 = x.right
    x.right = y
    y.left = t2
    x.height = max(getHeight(x.left), getHeight(x.right)) + 1
    y.height = max(getHeight(y.left), getHeight(y.right)) + 1
    return x

# Helper function to insert new elements maintaining the balance factor
def insert(root, key):
    if not root:
        return TreeNode(key)
    elif key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    
    root.height = max(getHeight(root.left), getHeight(root.right)) + 1
    balance = getBalance(root)

    # Case 1 - Left Left (LL)
    if balance > 1 and key < root.left.key:
        return rightRotate(root)

    # Case 2 - Right Right (RR)
    if balance < -1 and key > root.right.key:
        return leftRotate(root)

    # Case 3 - Left Right (LR)
    if balance > 1 and key > root.left.key:
        root.left = leftRotate(root.left)
        return rightRotate(root)

    # Case 4 - Right Left (RL)
    if balance < -1 and key < root.right.key:
        root.right = rightRotate(root.right)
        return leftRotate(root)

    return root

# search Function
def search(root, target):
    if not root:
        return
    
    if target == root.key:
        return True
    elif target < root.key:
        return search(root.left, target)
    elif target > root.key:
        return search(root.right, target)

def deleteNode(root, key):
    if not root:
        return None
    
    if key > root.key:
        root.right = deleteNode(root.right, key)

    elif key < root.key:
        root.left = deleteNode(root.left, key)

    else:
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left
        
        swapTarget = root.right
        
        while swapTarget.left:
            swapTarget = swapTarget.left
        
        root.key = swapTarget.key 
        root.right = deleteNode(root.right, swapTarget.key)
    
    root.height = max(getHeight(root.left), getHeight(root.right)) + 1
    balance = getBalance(root)

    # AVL Rotaation Cases
    if balance > 1 and key < root.left.key:
        return rightRotate(root)

    if balance < -1 and key > root.right.key:
        return leftRotate(root)

    if balance > 1 and key > root.left.key:
        root.left = leftRotate(root.left)
        return rightRotate(root)

    if balance < -1 and key < root.right.key:
        root.right = rightRotate(root.right)
        return leftRotate(root)

    return root

# Level Order Traversal
def levelOrder(root):
    if not root:
        return
    
    queue = deque()
    queue.append(root)
    while queue:
        current = queue.popleft()
        print(current.key, end=" ")
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

# Inorder Traversal
def inOrder(root):
    if not root:
        return
    inOrder(root.left)
    print(root.key, end=" ")
    inOrder(root.right)

# Test Values and function calls
root = None
keys = [10, 20, 30, 40, 50, 25]
for key in keys:
    root = insert(root, key)

levelOrder(root)
print()
inOrder(root)
print()
print(search(root, 40))
root = deleteNode(root, 30)
root = deleteNode(root, 10)
inOrder(root)