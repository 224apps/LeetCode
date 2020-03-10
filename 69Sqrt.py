class Solution(object):
    def mySqrt(self, x):
        """"
        :type x: int
        :rtype: int
        """
        if x == 0 or x == 1:
            return x
        s = 1
        while True:
            if s * s > x:
                return s-1
            s += 1
        return -1
            
    