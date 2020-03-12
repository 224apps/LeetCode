# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curr = head
        while curr != None and curr.next != None:
            curr.val, curr.next.val = curr.next.val, curr.val
            curr = curr.next.next
        return head
                