'''
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"
Note:

The length of both num1 and num2 is < 110.
Both num1 and num2 contain only digits 0-9.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
'''

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        res = [0] * (len(num1) + len(num2)) 
        pos = len(res) - 1

        for n1 in reversed(num1):
            tempPos = pos
            for n2 in reversed(num2):
                res[tempPos] += int(n1) * int(n2)
                res[tempPos - 1] += res[tempPos] // 10  
                res[tempPos] %= 10  
                tempPos -= 1
            pos -= 1

        st = 0
        while st < len(res) - 1 and res[st] == 0: 
            st += 1
        return ''.join(map(str, res[st:])) 
