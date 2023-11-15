# LINK : https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# optimal solution  
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        
        fast = dummy
        slow = dummy

        for _ in range(n+1):
            slow = slow.next

        while slow:
            fast = fast.next
            slow = slow.next
        
        fast.next = fast.next.next

        return dummy.next

# my first solution 
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        current = head

        # count lenght of linkedlist
        while current.next:
            current = current.next
            length+=1
        
        n = length - n
        if n < 0 and length != 0:
            head = head.next
            return head

        temp = head
        for i in range(n):
            temp = temp.next
        
        if temp.next:
            temp.next = temp.next.next
            return head
