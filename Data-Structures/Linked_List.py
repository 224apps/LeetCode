class Node:
    def __init__(self, data):
        self.data = data
        self.next = None 

class LinkedList:
    def __init__(self):
        self.head = None 
    
    #  insert a new node at the beginning 
    def insert_at_begin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    #  Inserts a new node after the given prev_node

    def insertAfter(self, prev, data):
        new_node = Node(data)

        if not prev:
            print("prev must be in the node")
            return
        new_node = Node(data)
        curr= self.head
        while curr:
            if curr != prev:
                curr = curr.next
        new_node.next = prev.next
        prev.next = new_node

    def insertAtEnd(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        curr = self.head
        while curr.next:
            curr = curr.next
        self.head.next = new_node

    # Given a reference to the head of a list  
    # and a position, delete the node at a given position
    def deleteNode(self, position):
        if not self.head:
            return 
        curr = self.head
        if position == 0:
            self.head = curr.next
            curr = None 
            return
        for index in range(position -1):
            curr = curr.next
            if curr is None:
                break
        if curr is None:
            return
        next = curr.next.next
        curr.next = None
        curr.next = next


    # This function prints contents of linked list 
    # starting from head
    def printList(self):
        temp = self.head
        res = []
        while temp:
           res.append(temp.data)
           temp = temp.next
        return res

    
        

        
            
        

    
    


# Start with the empty list 


llist = LinkedList() 
llist.insert_at_begin(6) 
llist.insert_at_begin(6)
llist.insert_at_begin(1)
llist.insertAtEnd(4)
llist.insertAtEnd(9)
llist.insertAfter(llist.head.next, 8) 
llist.printList() 
print("Created Linked List: ")
llist.printList() 
llist.deleteNode(4) 
print ("\nLinked List after Deletion at position 4: ")
llist.printList()