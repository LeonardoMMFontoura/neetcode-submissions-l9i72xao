class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        indegree = [0] * numCourses
        for u,v in prerequisites:
            adj[u].append(v)
            indegree[v]+=1
        res = []
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        while queue:
            course = queue.popleft()
            res.append(course)
            for other_course in adj[course]:
                indegree[other_course] -=1
                if indegree[other_course] == 0:
                    queue.append(other_course)
        return len(res) == numCourses