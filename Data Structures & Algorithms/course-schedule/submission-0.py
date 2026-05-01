class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i: [] for i in range(numCourses)}
        indegree = {i: 0 for i in range(numCourses)}
        for u,v in prerequisites:
            adj[v].append(u)
            indegree[u] +=1
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        count = 0
        while queue:
            curr = queue.popleft()
            count+=1
            for neighbor in adj.get(curr, []):
                if indegree[neighbor] != 0:
                    indegree[neighbor]-=1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        return count == numCourses