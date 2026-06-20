class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        deg = [0] * numCourses
        graph = [[] for _ in range(numCourses)]

        for course, pre in prerequisites:
            graph[pre].append(course)
            deg[course] += 1

        q = deque()
        order = []

        for course in range(len(deg)):
            if deg[course] == 0:
                q.append(course)
                order.append(course)

        while q:
            pre = q.popleft()
            for course in graph[pre]:
                deg[course] -= 1
                if deg[course] <= 0:
                    q.append(course)
                    order.append(course)
        
        return order if len(order) == numCourses else []