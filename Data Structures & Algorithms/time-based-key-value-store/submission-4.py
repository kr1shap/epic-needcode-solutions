class TimeMap:

    def __init__(self):
        self.hashmap = dict() 
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashmap: 
            self.hashmap[key] = []
        self.hashmap[key].append([value, timestamp])
        # print(self.hashmap)
        return
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashmap:
            return ""
        arr = self.hashmap[key]
        # print(arr)
        # search for the key and if its there return else return most recent element 
        left = 0
        right = len(arr)-1
        mid = (left+right)//2
        while left <= right: 
            mid = (left+right)//2
            if arr[mid][1] == timestamp: 
                return arr[mid][0]
            if arr[mid][1] > timestamp: #arr timestamp too large 
                right = mid - 1
            else: # arr timestamp too small 
                left = mid + 1
        if arr[right][1] > timestamp: 
            return ""
        else: 
            return arr[right][0]
