class Solution(object):
    def reverse(self, x):
        result = 0
        remaining = abs(x)
        
        while remaining != 0:
            result *= 10
            result += remaining % 10
            remaining /= 10
            
        minValue = -(2**31 -1) 
        maxValue = (2**31 -1)
            
        if result< minValue or result > maxValue:
            return 0
        else:
            return -result if x< 0 else result