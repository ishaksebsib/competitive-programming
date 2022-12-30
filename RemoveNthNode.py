
def removeNthFromEnd(self, head, n):
    first = second = head
    for _ in range(n):
        first = first.next
    if not first:
        return head.next
    while first.next:
        first = first.next
        second = second.next
    second.next = second.next.next

    return head