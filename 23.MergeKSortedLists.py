'''
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
'''















# Definition for singly-linked list.

from heapq import heappush, heappop
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heap = []
        head = point = ListNode(0)
        for elem in lists:
            if elem:
                heapq.heappush(heap, (elem.val, elem))
        
        while heap:
            value, node = heapq.heappop(heap)
            head.next = ListNode(value)
            head = head.next
            node = node.next
            if node:
                heapq.heappush(heap, (node.val, node))
        return point.next
    
    
    
#Solution II:   
    
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        def merge2Lists(l1, l2):
        	head = point = ListNode(0)
        	while l1 and l2:
        		if l1.val <= l2.val:
        			point.next = ListNode(l1.val)
        			l1 = l1.next
        		else:
        			point.next = ListNode(l2.val)
        			l2 = l2.next
        		point = point.next

        	if l1:
        		point.next = l1
        	else:
        		point.next = l2
        	return head.next

        if not lists:
        	return lists

        interval = 1
        while interval < len(lists):
        	for index in range(0, len(lists) - interval ,interval*2):
        		lists[index] = merge2Lists(lists[index], lists[index+interval])

        	interval *= 2

        return lists[0]