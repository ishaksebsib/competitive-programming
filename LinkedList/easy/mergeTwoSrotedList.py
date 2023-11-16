# LINK : https://leetcode.com/problems/merge-two-sorted-lists/description/

# updated code


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        dummy = res

        while list1 and list2:
            if list1.val >= list2.val:
                dummy.next = ListNode(list2.val)
                list2 = list2.next
                
            else:
                dummy.next = ListNode(list1.val)
                list1 = list1.next
                
            dummy = dummy.next

        # if there is left over add it to the end 
        if list1 or list2:
            dummy.next = list1 if list1 else list2

        return res.next

# the old one 

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

