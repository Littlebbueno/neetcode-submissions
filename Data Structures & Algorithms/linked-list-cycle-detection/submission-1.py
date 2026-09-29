# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from collections import deque
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        mySet = set()
        queue = deque()
        queue.append(head)
        while queue:
            node = queue.pop()
            if node not in mySet:
                mySet.add(node)
                if node.next:
                    queue.append(node.next)
            else:
                return True

        return False


