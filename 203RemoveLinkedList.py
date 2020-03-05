# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummyHead = ListNode("None")
        dummyHead.next = head
        
        curr = dummyHead
        
        while curr:
            if  curr.next and curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return dummyHead.next