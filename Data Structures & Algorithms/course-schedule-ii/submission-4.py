from collections import defaultdict
from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        inDegree = [0 for _ in range(numCourses)]
        adjList = defaultdict(list)
        for a, b in prerequisites: 
            inDegree[a]+=1
            adjList[b].append(a)

        # topo
        que = deque()
        res = []
        # add all ele with 0 in deg in que
        for i in range(len(inDegree)): 
            if inDegree[i] == 0: 
                que.append(i)
        # now preform result 
        while que: 
            ele = que.popleft()
            res.append(ele)
            for neigh in adjList[ele]:
                inDegree[neigh]-=1
                if inDegree[neigh] <= 0: 
                    que.append(neigh)
        if len(res) != numCourses: 
            return []
        return res


        