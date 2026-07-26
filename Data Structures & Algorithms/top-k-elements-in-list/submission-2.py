class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        eleCount = {} #dict mapping element: count
        count = [set() for _ in range(len(nums)+1)]#at most nums unique elements
        for num in nums:
            if num not in eleCount: 
                eleCount[num] = 1
                count[1].add(num)
                continue
            count[eleCount[num]].remove(num)
            count[eleCount[num]+1].add(num)
            eleCount[num]+=1  
        #now generate the final result 
        print(count)
        res = [] #max k length
        for i in range(len(count)-1, 0, -1): #ignore zero
            if(len(res) == k):
                return res
            res.extend(list(count[i]))
        return res

            
        