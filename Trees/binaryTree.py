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

print(preOrder(nodeA))
print(inOrder(nodeA))
print(postOrder(nodeA))
print(levelOrder(nodeA))
print(findHeight(nodeA))
mirrorTree(nodeA)
print(levelOrder(nodeA))
print("Exists" if search(nodeA, 'F') == True else "Does not exists")