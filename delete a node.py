def deleteNode(head, position):
    if position == 0:
        head = head.next
    else:
        aux = head
        contador = 1
        while aux is not None and contador < position:
            temp = temp.next 
            contador += 1
        aux.next = aux.next.next
    return head
        