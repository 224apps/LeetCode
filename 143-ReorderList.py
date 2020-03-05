# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        #Let's find the middle
        slow = fast = head
        
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        #Now let's split the list in two
        secondHead = self.reverseList(slow.next)
        slow.next = None
        
        #Now, let's have the two head
        
        curr1 = head
        curr2 = secondHead
        
        while curr2:
            currNext = curr1.next
            curr2Next = curr2.next
            
            curr1.next = curr2
            curr2.next = currNext
            
            curr1 = currNext
            curr2 = curr2Next
            
    
    def reverseList(self, head):
        prev = None

        curr = head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

        