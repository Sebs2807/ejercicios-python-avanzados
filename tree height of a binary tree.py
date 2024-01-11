class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

def height(root):
    if root is None:
        return -1
    else:
        return 1 + max(height(root.left),height(root.right))
