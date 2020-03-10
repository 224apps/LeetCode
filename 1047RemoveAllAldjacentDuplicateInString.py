class Solution(object):
    def removeDuplicates(self, S):
        """
        :type S: str
        :rtype: str
        """
        stack = []
        if not S:
            return""
        
        for char in S:
            if not stack:
                stack.append(char)
            else:
                firstChar = stack[-1]
                if firstChar == char:
                    stack.pop()
                else:
                    stack.append(char)
        if not stack:
            stack.append(char)
        return "".join(stack)