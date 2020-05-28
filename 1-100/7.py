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
            
            
#class Solution(object):
#def reverse(self, x):
## Note that in Python -1 / 10 = -1
#res, isPos = 0, 1
#if x < 0:
#    isPos = -1
#    x = -1 * x
#while x != 0:
#    res = res * 10 + x % 10
#    if res > 2147483647:
#        return 0
#    x /= 10
#return res * isPos

