'''
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.
'''

#Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        
        """
        on = head
        length = 1
        while on:
            length += 1
            on = on.next
        leftIndex = length - n -1
        if leftIndex == 0:
            return head.next
        on = head
        while leftIndex > 1:
            leftIndex -= 1
            on = on.next
        on.next = on.next.next

        return head
