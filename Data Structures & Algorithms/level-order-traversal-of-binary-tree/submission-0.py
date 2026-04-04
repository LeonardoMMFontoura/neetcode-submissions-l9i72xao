# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        fila = deque([root])
        res = []

        while fila:
            nivel_atual = []
            for _ in range(len(fila)):
                curr = fila.popleft()
                nivel_atual.append(curr.val)
                if curr.left:
                    fila.append(curr.left)
                if curr.right:
                    fila.append(curr.right)
            res.append(nivel_atual)
        return res