# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: return True
        if not p: return False
        if not q: return False
        queueP = deque()
        queueQ = deque()
        queueP.append(p)
        queueQ.append(q)
        while len(queueQ) == len(queueP) and queueQ:
            nodeP = queueP.popleft()
            nodeQ = queueQ.popleft()
            if nodeP.val != nodeQ.val:
                return False
            if nodeP.left and nodeQ.left:
                queueP.append(nodeP.left)
                queueQ.append(nodeQ.left)
            if nodeP.right and nodeQ.right:
                queueP.append(nodeP.right)
                queueQ.append(nodeQ.right)
            if nodeP.left and not nodeQ.left:
                return False
            if not nodeP.left and nodeQ.left:
                return False
            if nodeP.right and not nodeQ.right:
                return False
            if not nodeP.right and nodeQ.right:
                return False
        return True

        