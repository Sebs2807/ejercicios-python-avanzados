class Stack:
    def __init__(self, cap=1500):
        self.__a = [None for _ in range(cap)]
        self.__top = 0

    def pop(self):
        if self.__top > 0:
            self.__top = self.__top - 1
            return self.__a[self.__top]
        else:
            return None

    def push(self, x):
        self.__a[self.__top] = x
        self.__top = self.__top + 1

    def size(self):
        return self.__top

def is_valid_expression(expression):
    stack = Stack()

    for char in expression:
        if char in '([':
            stack.push(char)
        elif char in ')]':
            if stack.size() == 0:
                return 'No'
            top = stack.pop()
            if (char == ')' and top != '(') or (char == ']' and top != '['):
                return 'No'

    if stack.size() == 0:
        return 'Yes'
    else:
        return 'No'

# Leemos el entero n desde la entrada estándar
n = int(input())
results = []

# Leemos las n cadenas de paréntesis y corchetes
for _ in range(n):
    expression = input()
    result = is_valid_expression(expression)
    results.append(result)

# Imprimimos los resultados
for result in results:
    print(result)
