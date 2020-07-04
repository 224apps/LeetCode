'''
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example 1:

Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"
Example 2:

Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"
'''
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack, result = [-1], 0

        for index in range(len(s)):
        	if s[index] == '(':
        		stack.append(index)
        	else:
        		currIndex = stack.pop()
        		if currIndex == -1:
        			stack.append(index)
        		else:
        			result = max(result, index-currIndex+1)
        return result


# class Solution(object):
#     def longestValidParentheses(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         q = []
#         start, ans = 0, 0
#         for i in range(len(s)):
#             if s[i] == '(':
#                 q.append(i)
#                 continue
#             if not q: 
#                 start = i + 1
#             else:
#                 q.pop()
#             ans = max(ans, i - q[-1] if q else i - start + 1)
#         return ans
            