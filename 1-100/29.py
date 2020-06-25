'''
Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero, which means losing its fractional part. For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.

Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = truncate(3.33333..) = 3.
Example 2:

Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = truncate(-2.33333..) = -2.
Note:

Both dividend and divisor will be 32-bit signed integers.
The divisor will never be 0.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 231 − 1 when the division result overflows.
'''
mint = -pow(2, 31)
maxt = pow(2, 31) - 1

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        
        sign1 = (1 if dividend > 0 else -1)  
        sign2 = (1 if divisor > 0 else -1) 
        
        sign = -1 if sign1 + sign2 == 0 else 1
        
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        if dividend < divisor:
            return 0
        
        if divisor == 1:
            return max(mint, min(maxt, dividend if sign == 1 else -dividend))
        
        # find number of digits
        num = dividend
        k = 0
        while num >= 1:
            k+=1
            num >>= 1
        
        res = 0
        for n in range(k-1, -1, -1):
            s = dividend >> n
            
            if s < divisor:
                if res == 0:
                    continue
                res <<= 1 # don't shift unnecessarily if res == 0
            else:
                dividend -= divisor << n
                res <<= 1
                res += 1
         
        return max(mint, min(maxt, res if sign == 1 else -res))