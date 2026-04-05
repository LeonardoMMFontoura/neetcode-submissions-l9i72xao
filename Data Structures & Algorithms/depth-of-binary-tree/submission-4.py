# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        fila = deque([root])
        count=0
        while fila:
            count+=1
            for _ in range(len(fila)):
                curr = fila.popleft()
                if curr.left:
                    fila.append(curr.left)
                if curr.right:
                    fila.append(curr.right)
        return count        
