'''
Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...
Example 1:

Input: "A"
Output: 1
Example 2:

Input: "AB"
Output: 28
Example 3:

Input: "ZY"
Output: 701
'''

class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.upper()
        LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        maps  = {}
        for i in range(26):
            maps[LETTERS[i]] = i+1
        col = 0
        for l in s:
            col = 26 * col + maps[l]
        return col