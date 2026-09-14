
class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

def getHeight(node):
    if node is None:
        return -1
    return node.height

def getBalance(root):
    if not root:
        return
    return getHeight(root.left) - getHeight(root.right)

def leftRotate(x):
    y = x.right
    t2 = y.left
    y.left = x
    x.right = t2
    x.height = max(getHeight(x.left), getHeight(x.right)) + 1
    y.height = max(getHeight(y.left), getHeight(y.right)) + 1
    return y

def rightRotate(y):
    x = y.left
    t2 = x.right
    x.right = y
    y.left = t2
    x.height = max(getHeight(x.left), getHeight(x.right)) + 1
    y.height = max(getHeight(y.left), getHeight(y.right)) + 1
    return x

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

def levelOrder(root):
    if not root:
        return
    
    from collections import deque

    queue = deque()
    queue.append(root)
    while queue:
        current = queue.popleft()
        print(current.key, end=" ")
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

def inOrder(root):
    if not root:
        return
    inOrder(root.left)
    print(root.key, end=" ")
    inOrder(root.right)

root = None
keys = [10, 20, 30, 40, 50, 25]
for key in keys:
    root = insert(root, key)

print(levelOrder(root))
print(inOrder(root))
