class Node:
#Definición del árbol, como un nodo que puede moverse a la derecha e izquierda
    def __init__(self, value=None):
        self.value = value
        self.right = None
        self.left = None

#Función para obtener el valor del nodo, es el equivalente de x.key()
    def getValue(self):
        return self.value

#Función para darle valor a un nodo
    def setValue(self, new_value):
        self.value = new_value

#Función para obtener el nodo de la derecha
    def getRight(self):
        return self.right

#Función para obtener el valor de la izquierda
    def getLeft(self):
        return self.left

#Función para ir al valor de la derecha
    def setRight(self, right):
        if isinstance(right, Node) or right is None:
            self.right = right

#Función para ir al valor de la izquierda
    def setLeft(self, left):
        if isinstance(left, Node) or left is None:
            self.left = left

class Binary_Tree:
#Agregación de valores a un árbol
    def __init__(self, data=[]):
        self.root = None
        for e in data:
            self.insert(e)

#Función que inserta un valor en un árbol
    def insert(self, value):
        new_node = Node(value)
        y = None
        x = self.getRoot()
        while x is not None:
            y = x
            if value < x.getValue():
                x = x.getLeft()
            else:
                x = x.getRight()
        if y is None:
            self.root = new_node
        elif value < y.getValue():
            y.setLeft(new_node)
        else:
            y.setRight(new_node)

#Función que obtiene el mínimo de un árbol (auxiliar para la eliminación de valores)
    def minimum(self, node):
        while node.getLeft() is not None:
            node = node.getLeft()
        return node

#Función TRANSPLANT que se encarga cambiar los valores de los hijos por los del padre para la eliminación
    def transplant(self, node1, node2):
        if node1 is None:
            self.root = node2
        elif node1 == node1.getLeft():
            node1.setLeft(node2)
        else:
            node1.setRight(node2)

#Función para eliminar un valor del árbol, llama a la función auxiliar TRANSPLANT
    def delete(self, node):
        if node.getLeft() is None:
            self.transplant(node, node.getRight())
        elif node.getRight() is None:
            self.transplant(node, node.getLeft())
        else:
            y = self.minimum(node.getRight())
            if y != node:
                self.transplant(y, y.getRight())
                y.setRight(node.getRight())
            self.transplant(node, y)
            y.setLeft(node.getLeft())

#Función para buscar un valor en el árbol
    def search(self, value):
        value = Node(value)
        node = self.root
        while node is not None and value.getValue() != node.getValue():
            if value.getValue() < node.getValue():
                node = node.getLeft()
            else:
                node = node.getRight()
        return node

#Función para actualizar un valor del árbol
    def update(self, new_value, old_value):
        origin = self.search(old_value)
        if origin is not None:
            origin.setValue(new_value)

#Función para obtener la raiz del árbol
    def getRoot(self):
        return self.root

#Función inorden
    def inorden_recursivo(self, nodo):
        if nodo is not None:
            self.inorden_recursivo(nodo.getLeft())
            print(nodo.getValue(), end=", ")
            self.inorden_recursivo(nodo.getRight())

#Función preorden
    def preorden_recursivo(self, nodo):
        if nodo is not None:
            print(nodo.getValue(), end=", ")
            self.preorden_recursivo(nodo.getLeft())
            self.preorden_recursivo(nodo.getRight())

#Función postorden
    def postorden_recursivo(self, nodo):
        if nodo is not None:
            self.postorden_recursivo(nodo.getLeft())
            self.postorden_recursivo(nodo.getRight())
            print(nodo.getValue(), end=", ")

#Función que llama a la función postorden para imprimir el árbol en postorden
    def postorden(self):
        print("Postorden:")
        self.postorden_recursivo(self.root)
        print()

#Función que llama a la función inorden para imprimir el árbol en inorden
    def inorden(self):
        print("Inorden:")
        self.inorden_recursivo(self.root)
        print()

#Función que llama a la función preorden para imprimir el árbol en preorden
    def preorden(self):
        print("Preorden:")
        self.preorden_recursivo(self.root)
        print()

# Crear el árbol y agregar elementos
data = [5, 3, 7, 2, 4, 6, 8]
tree = Binary_Tree(data)

# Imprimir en los tres tipos de recorrido
tree.postorden()
tree.inorden()
tree.preorden()

#El tiempo total invertido en el laboratorio fue de alrededor de 5 horas
#El laboratorio está completo
#El mayor logro fue definir una clase para una estructura de datos, cosa que no habiamos hecho nunca
#El mayor problema técnico fue poder probar que todo el código estuviera correcto, mediante la impresión en los 3 diferentes ordenes, ya que era muy extraño trabajando sin un main()