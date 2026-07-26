class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #create adj list 
        adjL = {}
        for i in range(numCourses):
            adjL[i] = []
        #now add courses
        for preReq in prerequisites:
            adjL[preReq[0]].append(preReq[1])
        
        #now, we have a graph where a course has a directed edge pointing to its pre reqs 
        #we want to preform DFS
            #in DFS, we have a visited array to keep track of alr seen nodes 
            #in a valid tree, we would have no already seen nodes 
            #but in an invalid tree (i.e cyclic) we will see a cycle (alr seen)
        visited = set()
        visiting = set()

        def dfs(i):
            if i in visiting:
                return False
            if i in visited:
                return True
            visiting.add(i)
            for course in adjL[i]:
                if not dfs(course):
                    return False
            visiting.remove(i)
            visited.add(i)
            return True

        #preform dfs on all nodes from i to n 
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True