def reverse(llist):
    while llist.next is not None:
        llist.next,llist.prev,llist = llist.prev,llist.next,llist.next
    llist.next,llist.prev = llist.prev,None
    return llist