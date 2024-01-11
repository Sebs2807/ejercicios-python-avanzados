def insertNodeAtPosition(llist, data, position):
    node = SinglyLinkedListNodellist(data)
    if llist == None:
        llist = node
    else:
        aux = llist
        contador = 1
        while aux is not None and contador < position:
            aux = aux.next
            contador += 1
        node.next = aux.next
        aux.next = node
    return llist
        