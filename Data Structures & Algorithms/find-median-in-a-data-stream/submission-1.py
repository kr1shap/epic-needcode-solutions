import bisect
import heapq
class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []
        
    def addNum(self, num: int) -> None:
        # bisect.insort(self.arr, num)
        if self.left and -self.left[0] > num:
            heapq.heappush(self.left, -num)
        else:
            heapq.heappush(self.right, num)
        # rebalance
        while len(self.left) - len(self.right) > 1: 
            ele = heapq.heappop(self.left)
            heapq.heappush(self.right, -ele)
        while len(self.right) - len(self.left) > 1: 
            ele = heapq.heappop(self.right)
            heapq.heappush(self.left, -ele)
        return

    def findMedian(self) -> float:
        if not self.right and not self.left: 
            return 0
        if len(self.right) > len(self.left):
            return self.right[0]
        elif len(self.left) > len(self.right):
            return -self.left[0]
        return (-self.left[0]+self.right[0]) / 2
        # if not self.arr: 
        #     return 0
        # if len(self.arr) % 2 == 0: 
        #     # even length [1, 2, 3, 4] (take mean of middle 2)
        #     mid = len(self.arr) // 2
        #     mean = (self.arr[mid] + self.arr[mid-1]) / 2
        #     return mean
        # return self.arr[len(self.arr)//2]
        
        