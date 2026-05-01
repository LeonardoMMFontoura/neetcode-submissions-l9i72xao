class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        res = []
        for u, v in prerequisites:
            adj[v].append(u)
            indegree[u]+=1
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        while queue:
            curr = queue.popleft()
            res.append(curr)
            for neighbor in adj[curr]:
                indegree[neighbor] -=1
                if indegree[neighbor] ==0:
                    queue.append(neighbor)
        return res if numCourses == len(res) else []
