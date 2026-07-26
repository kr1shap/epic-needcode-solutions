class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        path = []
        
        #create adj list 
        adjL = {}
        for i in range(numCourses):
            adjL[i] = []
        for pre in prerequisites:
            adjL[pre[0]].append(pre[1])

        visiting = set()
        visited = set()

        def dfs(node):
            if node in visiting:
                path.insert(0, node)
                return False
            if node in visited:
                return True
            visiting.add(node)
            for nei in adjL[node]:
                if not dfs(nei):
                    path.insert(0, node)
                    return False
            visiting.remove(node)
            visited.add(node)
            path.append(node)
            return True

        #preform dfs
        for i in range(numCourses):
            if not dfs(i):
                return []
        return path
            
