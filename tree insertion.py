    def insert(self, val):
        new_node = Node(val)
        if self.root is None:
            self.root = new_node 
            return
        actual = self.root
        while actual:
            if val < actual.info:
                if actual.left is None:
                    actual.left = new_node
                    return
                actual = actual.left
            else:
                if actual.right is None:
                    actual.right = new_node
                    return
                actual = actual.right
