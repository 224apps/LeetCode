class Node:
    def __init__(self, next=None, prev=None, data= None):
        self.next = next
        self.prev = prev
        self.data = data

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def  insert_at_begin(self,  data):
        node = Node(data)
        node.next = self.head
        if self.head:
            self.head.prev = node
        self.head = node 
    
    def insert_after(self, prev_node, data):
        if not prev:
            print("This node is not present in the list")
            return
        node = Node(data)
        
        node.next = prev_node.next
        prev_node.next  = node
        node.prev = prev_node

        if node.next:
            node.next.prev = node

    def insert_at_end(self, data):

        node = Node(data)
        last = self.head

        
    


