class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = { i:[] for i in range(numCourses)}
        for course, pre in prerequisites:
            preMap[course].append(pre)

        visited = set()
        res = set()
        order = []

        def dfs(course: int) -> bool:
            if course in visited:
                return False
            if len(preMap[course]) == 0:
                if course not in res:
                    order.append(course)
                    res.add(course)
                return True

            visited.add(course)

            for pre in preMap[course]:
                if not dfs(pre):
                    return False
            
            if course not in res:
                order.append(course)
                res.add(course)
            visited.remove(course)
            preMap[course] = []
            
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return []
            
        return order