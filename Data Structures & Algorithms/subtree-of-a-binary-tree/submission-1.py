# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        queue = deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            if node.val == subRoot.val:
                subQueue = deque()
                subRootQueue = deque()
                subRootQueue.append(subRoot)
                subQueue.append(node)
                controlVar = True
                while subRootQueue:
                    subNode = subQueue.popleft()
                    subRootNode = subRootQueue.popleft()
                    if subNode.val != subRootNode.val:
                        controlVar = False
                        break
                    # Lado direito
                    if subRootNode.right and subNode.right:
                        subQueue.append(subNode.right)
                        subRootQueue.append(subRootNode.right)
                    if subRootNode.right and not subNode.right:
                        controlVar = False
                        break
                    if not subRootNode.right and subNode.right:
                        controlVar = False
                        break
                    # Lado esquerdo
                    if subRootNode.left and subNode.left:
                        subQueue.append(subNode.left)
                        subRootQueue.append(subRootNode.left)
                    if subRootNode.left and not subNode.left:
                        controlVar = False
                        break
                    if not subRootNode.left and subNode.left:
                        controlVar = False
                        break
                if controlVar == True:
                    return True
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
        return False
            



        