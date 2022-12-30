def reverseList(head):
  
    reversed = None
    prev = None

    while head != None:
        reversed = head
        head = head.next
        reversed.next = prev
        prev = reversed
        
    return reversed
