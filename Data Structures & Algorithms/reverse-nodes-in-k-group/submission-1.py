# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]: 

        def reverseList(head: Optional[ListNode], end: Optional[ListNode]): 
            if head == None: 
                return None
            dummy = end
            curr = head 
            temp = curr
            while curr != end:
                # set temp var 
                temp = curr
                curr = curr.next
                # move its next ptr after incrementing curr to not lose
                temp.next = dummy
                dummy = temp 
            return temp

        res = head
        curr = head
        prev = None
        while curr != None:
            temp = curr
            count = 0 
            while count < k:
                if temp == None: 
                    return res # only do for len = k 
                temp = temp.next
                count+=1
            # now call reverse list
            prevCurr = curr 
            if curr == head:
                curr = reverseList(curr, temp)
                res = curr
            else: 
                curr = reverseList(curr, temp)
                prev.next = curr
            
            # for i in range(k):
            prev = prevCurr
            curr = prevCurr.next
            
        return res




            
            
        

    