# LINK : https://leetcode.com/problems/remove-nth-node-from-end-of-list/

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
