'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
 

Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
'''

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minimum = float('inf')
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if not self.stack:
            self.stack.append(x)
            self.minimum = x
        else:
            if x < self.minimum:
                self.stack.append(2*x - self.minimum)
                self.minimum = x
            else:
                self.stack.append(x)
        
        
    def pop(self):
        """
        :rtype: None
        """
        if self.stack:
            top = self.stack.pop()
            if top < self.minimum:
                self.minimum =  2* self.minimum - top
        

    def top(self):
        """
        :rtype: int
        """
        if not self.stack:
            return None
        else:
            top = self.stack[-1]
            if top < self.minimum:
                return self.minimum
            else:
                return top
        

    def getMin(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.minimum
        else:
            return None
        
