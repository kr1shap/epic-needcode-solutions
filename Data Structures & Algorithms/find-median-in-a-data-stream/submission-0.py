import bisect
class MedianFinder:

    def __init__(self):
        self.arr = []
        
    def addNum(self, num: int) -> None:
        bisect.insort(self.arr, num)

    def findMedian(self) -> float:
        if not self.arr: 
            return 0
        if len(self.arr) % 2 == 0: 
            # even length [1, 2, 3, 4] (take mean of middle 2)
            mid = len(self.arr) // 2
            mean = (self.arr[mid] + self.arr[mid-1]) / 2
            return mean
        return self.arr[len(self.arr)//2]
        
        