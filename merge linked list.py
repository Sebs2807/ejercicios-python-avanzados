def mergeLists(head1, head2):
    if head1 == head2 == None:
        return None
    if head1 == None:
        return head2
    if head2 == None:
        return head1
    if head1.data < head2.data:
        aux = head1
        aux.next = mergeLists(head1.next,head2)
    else:
        aux = head2
        aux.next = mergeLists(head1,head2.next)
    return aux
