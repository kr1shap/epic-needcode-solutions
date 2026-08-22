class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = dict() # map freq -> set(num)
        hashmap2 = dict() #map num -> freq
        for ele in nums: 
            if ele in hashmap2: 
                freq = hashmap2[ele]
                hashmap2[ele]+=1
                hashmap[freq].remove(ele)
                freq+=1
                if freq not in hashmap: 
                    hashmap[freq] = set()
                hashmap[freq].add(ele)
            else: 
                hashmap2[ele] = 1
                if 1 not in hashmap: 
                    hashmap[1] = set()
                hashmap[1].add(ele)
        
        # only have to iterate through len(nums) times
        count = 0
        res = []
        for i in range(len(nums), -1, -1): 
            if count >= k: 
                return res
            if i in hashmap: 
                elements = list(hashmap[i])
                res.extend(elements)
                count+=len(elements)
        return res


                    