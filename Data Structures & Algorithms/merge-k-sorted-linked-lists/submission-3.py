# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #create heap 
        lst = []
        for i in range(len(lists)): 
            if lists[i] != None:
                lst.append((lists[i].val, i, lists[i]))
        heapq.heapify(lst)
        head = None
        curr = head
        while len(lst) > 0: 
            (val, i, item) = heapq.heappop(lst)
            if head == None: 
                head = item
                curr = head
            else: 
                curr.next = item
                curr = curr.next
            if item.next != None: 
                heapq.heappush(lst, (item.next.val, i, item.next))
        return head


            