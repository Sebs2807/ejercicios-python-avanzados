def findMergeNode(head1, head2):
    def longitudes(head):
        length = 0
        while head.next is not None:
            head = head.next
            length += 1
        return length
    def comun(diff,head1,head2):
        for i in range(diff):
            head1 = head1.next
        while head1 and head2:
            if head1 == head2:
                return head1.data
            else:
                head1 = head1.next
                head2 = head2.next
    len1 = longitudes(head1)
    len2 = longitudes(head2)
    if len1 > len2:
        return comun(len1 - len2,head1,head2)
    else:
        return comun(len2 - len1,head2,head1)
    