# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        res = ListNode()
        if list1.val <= list2.val:
            res.val = list1.val
            list1 = list1.next
        else:
            res.val = list2.val
            list2 = list2.next 
        finalRes = res
        
        while list1 or list2:
            if not list1 and list2:
                nxt = list2.next
                res.next = list2
                res = res.next
                list2 = nxt
            if list1 and not list2:
                nxt = list1.next
                res.next = list1
                res = res.next
                list1 = nxt
            if list1 and list2:
                if list1.val <= list2.val:
                    nxt = list1.next
                    res.next = list1
                    res = res.next
                    list1 = nxt
                else:
                    nxt = list2.next
                    res.next = list2
                    res = res.next
                    list2 = nxt
        return finalRes







        