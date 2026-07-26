class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ltof = {} #letter to frequency
        for num in nums:
            if num not in ltof:
                ltof[num] = 0
            ltof[num]+=1
        #create array, where an index i represents frequency
        freq_arr = [[] for i in range(len(nums)+1)]#we will not be using freq_arr[0]
        for num in ltof:
            freq_arr[ltof[num]].append(num) #maps freq -> [nums]
        #now iterate through frequency array, from high to low
        res = []
        for j in range(len(freq_arr)-1, 0,-1):
            if len(res)==k:
                return res
            res.extend(freq_arr[j])
        return res