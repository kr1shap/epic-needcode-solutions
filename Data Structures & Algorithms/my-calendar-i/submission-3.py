class Node: 
    def __init__(self, interval: List[int]):
        # we use interval[0] as minkey 
        self.key = interval[0]
        self.interval = interval 
        self.left = None
        self.right = None 

class MyCalendar:
    
    def __init__(self):
        self.root = None
        
    def book(self, startTime: int, endTime: int) -> bool:
        isBooked = False
        interval = [startTime, endTime]
        #preform search 

        def search(root: Node) -> Node: 
            nonlocal isBooked
            if root is None: 
                node = Node(interval)
                isBooked = True
                return node 
            start = root.interval[0]
            end = root.interval[1]
            # case 1 is startTime is geq current interval, and less than end = overlap 
            # case 2 interval inside current interval 
            # case 3, 4
            if start <= startTime < end or start < endTime < end or (startTime <= start and endTime >= end) or (startTime >= start and endTime <= end): 
                # false
                print("false, ", interval)
                return root 
            elif startTime <= start: 
                root.left = search(root.left)
            else: 
                root.right = search(root.right)
            return root

        self.root = search(self.root)
        return isBooked


        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)