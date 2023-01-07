class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head     
        while temp != None and temp.next != None:
            while temp.val == temp.next.val:
                temp.next = temp.next.next
                if temp.next == None:
                    break
            temp = temp.next
        return head
