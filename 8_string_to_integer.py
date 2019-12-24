class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        isNegative = False
        if str and str[0] == '-':
            isNegative = True
        if str and (str[0] == '+' or str[0] == '-'):
            str = str[1:]
        if not str:
            return 0
        digits = { i for i in '0123456789'}
        result = 0
        for char in str:
            if char not in digits:
                break
            result = result * 10 + int(char)
        if isNegative:
            result = -result
            
        result = max(min(result,2**31 - 1),-2**31)
        return result