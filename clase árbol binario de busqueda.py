class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self._insert(self.root, value)

    def _insert(self, node, value):
        if node is None:
            return TreeNode(value)
        
        if value < node.value:
            node.left = self._insert(node.left, value)
        else:
            node.right = self._insert(node.right, value)
        
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))

        balance = self._get_balance(node)

        # Casos de desequilibrio
        if balance > 1:
            if value < node.left.value:
                return self._rotate_right(node)
            else:
                node.left = self._rotate_left(node.left)
                return self._rotate_right(node)
        if balance < -1:
            if value > node.right.value:
                return self._rotate_left(node)
            else:
                node.right = self._rotate_right(node.right)
                return self._rotate_left(node)

        return node

    def search(self, value):
        return self._search(self.root, value)

    def _search(self, node, value):
        if node is None:
            return False
        if value == node.value:
            return True
        if value < node.value:
            return self._search(node.left, value)
        else:
            return self._search(node.right, value)

    def balance(self):
        self.root = self._balance(self.root)

    def _balance(self, node):
        if node is None:
            return None

        node.left = self._balance(node.left)
        node.right = self._balance(node.right)

        balance = self._get_balance(node)

        if balance > 1:
            if self._get_balance(node.left) < 0:
                node.left = self._rotate_left(node.left)
            return self._rotate_right(node)
        if balance < -1:
            if self._get_balance(node.right) > 0:
                node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node

    def _get_height(self, node):
        if node is None:
            return 0
        return node.height

    def _get_balance(self, node):
        if node is None:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    def _rotate_left(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        return y

    def _rotate_right(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        x.height = 1 + max(self._get_height(x.left), self._get_height(x.right))

        return x

    def pre_order_traversal(self, node):
        if node:
            print(node.value, end=' ')
            self.pre_order_traversal(node.left)
            self.pre_order_traversal(node.right)

    def in_order_traversal(self, node):
        if node:
            self.in_order_traversal(node.left)
            print(node.value, end=' ')
            self.in_order_traversal(node.right)

    def post_order_traversal(self, node):
        if node:
            self.post_order_traversal(node.left)
            self.post_order_traversal(node.right)
            print(node.value, end=' ')

    def print_pre_order(self):
        self.pre_order_traversal(self.root)
        print()

    def print_in_order(self):
        self.in_order_traversal(self.root)
        print()

    def print_post_order(self):
        self.post_order_traversal(self.root)
        print()

# Ejemplo de uso:
avl_tree = AVLTree()
avl_tree.insert(5)
avl_tree.insert(3)
avl_tree.insert(7)
avl_tree.insert(2)
avl_tree.insert(4)
avl_tree.insert(6)
avl_tree.insert(8)

print("Recorrido en Pre-orden:")
avl_tree.pre_order_traversal(avl_tree.root)
print()

print("Recorrido en In-orden:")
avl_tree.in_order_traversal(avl_tree.root)
print()

print("Recorrido en Post-orden:")
avl_tree.post_order_traversal(avl_tree.root)
