# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        pilha = []
        curr = root
        count = 0

        while pilha or curr:
            while curr:
                pilha.append(curr)
                curr = curr.left
            curr = pilha.pop()
            count += 1
            if count == k:
                return curr.val
            curr = curr.right