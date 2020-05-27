
#Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Solution1:
# class Solution(object):
#     def middleNode(self, head):
#         """
#         :type head: ListNode
#         :rtype: ListNode
#         """
#         arrayOfLL = []
#         current = head
#         while current:
#             arrayOfLL.append(current)
#             current = current.next
#         copyOfArrayLL = arrayOfLL
#         return copyOfArrayLL[len(arrayOfLL) // 2]

Solution2:

class Solution(object):
    def middleNode(self, head):
        slow = fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
        