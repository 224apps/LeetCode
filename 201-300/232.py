class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.popStack = []
        self.pushStack = []

    def push(self, x):
        """
        Push element x to the back of queue.
        """
        self.pushStack.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        """
        self.peek()
        return self.popStack.pop()

    def peek(self):
        """
        Get the front element.
        """
        if not self.popStack:
            while self.pushStack:
                self.popStack.append(self.pushStack.pop())
        return self.popStack[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        """
        return  not self.pushStack and   not self.popStack
