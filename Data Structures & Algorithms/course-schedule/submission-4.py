class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # idea - > make adj list 
        # make adj list with pre req -> course 
        # from this, you can see if you can make a graph 
        hashmap = dict() 
        for req in prerequisites: 
            if req[0] not in hashmap: 
                hashmap[req[0]] = []
            hashmap[req[0]].append(req[1])

        visiting = set() 
        visited = set()
        def dfs(i): 
            if i in visited: 
                return False
            if i in visiting: 
                return True # cycle 
            visiting.add(i)
            if i not in hashmap: 
                visiting.remove(i)
                visited.add(i)
                return False
            for crs in hashmap[i]:
                if dfs(crs):
                    return True
            visiting.remove(i)
            visited.add(i)
        for i in range(numCourses):
            if dfs(i):
                return False
        return True


        
        
        