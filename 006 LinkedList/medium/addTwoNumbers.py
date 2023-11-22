# LINK : https://leetcode.com/problems/add-two-numbers/description/
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        res = ListNode()
        temp = res

        while l1 or l2:
            val = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            if val < 10:
                temp.next = ListNode(val)
                carry = 0
            else:
                temp.next = ListNode(val % 10)
                carry = 1

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            temp = temp.next

        if carry:
            temp.next = ListNode(carry)

        return res.next
