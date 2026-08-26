class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        hashmap = dict()
        for i in range(0, len(nums)):
            nums[i] = -nums[i]
            hashmap[i] = nums[i]
        heapq.heapify(nums)
        auxheap = []
        i = 1
        heapq.heappush(auxheap, (nums[0], 0))
        while i != k:
            (val, index) = heapq.heappop(auxheap)
            ind1 = 2*index + 1
            ind2 = 2*index + 2
            if ind1 < len(nums):
                heapq.heappush(auxheap, (nums[ind1], ind1))
            if ind2 < len(nums):
                heapq.heappush(auxheap, (nums[ind2], ind2))
            i+=1
        (val, index) = heapq.heappop(auxheap)
        return -val
