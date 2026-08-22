# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # make hashmap of nodes 
        index_to_node = dict()
        curr = head
        counter = 0
        while curr != None: 
            index_to_node[counter] = curr
            curr = curr.next
            counter+=1 

        # 0, n-1 = 3, 1, n-2 = 2
        # 0, n-1, 1, n-2
        # now do the change
        maxInd = (counter)//2
        # 0, n-1, 1, n-2, 2, n-3, 3
        # 0, n-1, 1, n-2 
        res = index_to_node[0]
        for i in range(1, maxInd + 1):
            end = counter - i 
            start = i 
            if start < end: 
                res.next = index_to_node[counter-i]
                res = res.next
            res.next = index_to_node[i]
            res = res.next
            # if start == end: 
        res.next = None
        head = res
