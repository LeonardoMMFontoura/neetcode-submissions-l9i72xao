"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def helper(row, col, size):
            first_value = grid[row][col]
            for r in range(row, row + size):
                for c in range(col, col + size):
                    if first_value != grid[r][c]:
                        half = size // 2
                        return Node(
                            val=True,
                            isLeaf=False,
                            topLeft=helper(row, col, half),
                            topRight=helper(row, col + half, half),
                            bottomLeft=helper(row + half, col, half),
                            bottomRight=helper(row + half, col + half, half)
                        )
            return Node(val=first_value,isLeaf=True)
        return helper(0,0,len(grid)) 
        