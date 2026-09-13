class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #map each element with its pre requisites
        mapping = {i: [] for i in range(numCourses)}
        for course, preReq in prerequisites:
            mapping[course].append(preReq)

        #dfs for each course
        visited = set()

        def dfs(course):
            if course in visited:
                return False
            if mapping[course]==[]:
                return True
            visited.add(course)
            for req in mapping[course]:
                if not dfs(req):
                    return False
            #if none of the pre reqs cause a cycle, mark as check and no pre req cause we checked everythign we can simply return without checking the whole tree again
            visited.remove(course)
            mapping[course]=[]
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
        


        
        