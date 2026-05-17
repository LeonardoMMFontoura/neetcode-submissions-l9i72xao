"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        cloned_graph = {node: Node(node.val)} 
        queue = deque([node])
        while queue:
            curr = queue.popleft()
            for neighbor in curr.neighbors:
                if neighbor not in cloned_graph:
                    cloned_graph[neighbor] = Node(neighbor.val) 
                    queue.append(neighbor) 
                cloned_graph[curr].neighbors.append(cloned_graph[neighbor])  
        return cloned_graph[node] 
        

