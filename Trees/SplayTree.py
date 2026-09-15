class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# Helper function to rotate the tree left at a given node
def leftRotate(x):
    y = x.right
    t2 = y.left
    y.left = x
    x.right = t2
    return y

# Helper function to rotate the tree right at a given node
def rightRotate(y):
    x = y.left
    t2 = x.right
    x.right = y
    y.left = t2
    return x

# Splay function to bring the key to the root if present
def splay(root, key):
    if not root or root.key == key:
        return root
        
    # Key lies in the left subtree
    if key < root.key:
        if not root.left:
            return root
            
        # Zig-Zig (Left Left)
        if key < root.left.key:
            root.left.left = splay(root.left.left, key)
            root = rightRotate(root)
        # Zig-Zag (Left Right)
        elif key > root.left.key:
            root.left.right = splay(root.left.right, key)
            if root.left.right:
                root.left = leftRotate(root.left)
                
        return root if not root.left else rightRotate(root)
        
    # Key lies in the right subtree
    else:
        if not root.right:
            return root
            
        # Zag-Zag (Right Right)
        if key > root.right.key:
            root.right.right = splay(root.right.right, key)
            root = leftRotate(root)
        # Zag-Zig (Right Left)
        elif key < root.right.key:
            root.right.left = splay(root.right.left, key)
            if root.right.left:  # Fixed the typo here
                root.right = rightRotate(root.right)
                
        return root if not root.right else leftRotate(root)

def insert(root, key):
    if not root:
        return TreeNode(key)
        
    root = splay(root, key)
    if root.key == key:
        return root
        
    node = TreeNode(key)
    if key < root.key:
        node.right = root
        node.left = root.left
        root.left = None
    else:
        node.left = root
        node.right = root.right
        root.right = None
    return node

def delete(root, key):
    if not root:
        return None
        
    root = splay(root, key)
    if root.key != key:
        return root  # Key not found
        
    if not root.left:
        return root.right
        
    # Splay the maximum element in the left subtree to the root of the left subtree
    leftSubTree = root.left
    while leftSubTree.right:
        leftSubTree = leftSubTree.right
        
    new_left = splay(root.left, leftSubTree.key)
    new_left.right = root.right
    return new_left

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

# Corrected Inorder Traversal
def inOrder(root):
    if not root:
        return
    inOrder(root.left)
    print(root.key, end=" ")
    inOrder(root.right)

# Execution
root = None
keys = [1, 2, 3, 4, 5, 6, 7, 8, 4.3]
for key in keys:
    root = insert(root, key)

inOrder(root)
print()
root = delete(root, 5)
inOrder(root)
print()
print(search(root, 4))