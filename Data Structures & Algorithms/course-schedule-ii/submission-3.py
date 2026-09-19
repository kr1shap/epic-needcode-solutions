class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        parent = [i for i in range(numCourses)]
        visiting = set()
        visited = set()

        # make adj list 
        hashmap = dict()
        for prereq in prerequisites: 
            if prereq[1] not in hashmap: 
                hashmap[prereq[1]] = []
            hashmap[prereq[1]].append(prereq[0])

        # dfs 
        path = []
        def dfs(i) -> bool: 
            if i in visited: 
                return 
            if i in visiting: 
                return True
            visiting.add(i)
            neighbours = hashmap[i] if i in hashmap else []
            for neigh in neighbours: 
                if dfs(neigh):
                    return True
                parent[neigh] = i
            visiting.remove(i)
            visited.add(i)
            path.append(i)

        for i in range(numCourses):
            if dfs(i):
                return []
        path.reverse()
        for i in range(numCourses):
            if i not in visited: 
                path.append(i)
        return path

