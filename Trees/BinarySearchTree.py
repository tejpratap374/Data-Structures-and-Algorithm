class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

def insert(root, key):
    if root is None:
        return TreeNode(key)
    else:
        if root.key < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

def search(root, key):
    if root is None or root.key == key:
        return root
    if root.key < key:
        return search(root.right, key)
    return search(root.left, key)

def inOrder(root):
    if root:
        inOrder(root.left)
        print(root.key, end=" ")
        inOrder(root.right)

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
        
    return root

    

root = None
keys = [10, 20, 45, 40, 5, 7, 25, 12, 6]
for key in keys:
    root = insert(root, key)

inOrder(root)
root = deleteNode(root, 20)
print()
inOrder(root)