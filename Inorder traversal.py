def inOrder(root):
    if root:
        inOrder(root.left)
        print(root, end = " ")
        inOrder(root.right)
        