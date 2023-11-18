# LINK : https://leetcode.com/problems/linked-list-cycle/


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                return True

        return False


# my way

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        is_exist = set()

        while head:
            if head in is_exist:
                return True
            is_exist.add(head)
            head = head.next
            
        return False
