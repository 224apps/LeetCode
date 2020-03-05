
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None
        
        hashTable = {}

        curr = head

        while curr:
            hashTable[curr] = Node(curr.val, None, None)
            curr = curr.next

        curr = head
        while curr:
            if curr.next:
                hashTable[curr].next = hashTable[curr.next]
            if curr.random:
                hashTable[curr].random = hashTable[curr.random]
            curr = curr.next

        return hashTable[head]

    

