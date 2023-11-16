# LINK : https://leetcode.com/problems/merge-two-sorted-lists/description/


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        dummy = res
        temp = list1
        temp2 = list2

        while temp and temp2:
            if temp.val >= temp2.val:
                dummy.next = ListNode(temp2.val)
                temp2 = temp2.next
                
            else:
                dummy.next = ListNode(temp.val)
                temp = temp.next
                
            dummy = dummy.next

        # if there is left over add it to the end 
        if temp or temp2:
            dummy.next = temp if temp else temp2

        return res.next

