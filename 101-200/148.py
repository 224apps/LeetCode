'''
Sort a linked list in O(n log n) time using constant space complexity.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4
Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        slow, fast =  head, head.next
        
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            
        head1, head2 = head, slow.next
        slow.next = None
        head1 = self.sortList(head1)
        head2 = self.sortList(head2)
        head = self.merge(head1, head2)
        return head
    
    def merge(self, h1, h2):
        if not h1:
            return h2
        if not h2:
            return h1
        result = ListNode(0)
        p = result
        
        while h1 and h2:
            if h1.val < h2.val:
                p.next = ListNode(h1.val)
                h1 = h1.next
                p = p.next
            else:
                p.next = ListNode(h2.val)
                h2 = h2.next
                p = p.next
        if h1:
            p.next = h1
        if h2:
            p.next=  h2
        return result.next
        
            
        