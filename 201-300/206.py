'''
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
'''

# iteratively
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        on = head
        prev = None
        while on:
            temp = on.next
            on.next = prev
            prev = on
            on = temp
        return prev

    def reverseListR(self, on, prev = None):

        if on is None:
            return prev
        temp = on.next
        on.next = prev
        return reverseListR(temp,on)


