class Solution(object):
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        direction = 0
        
        for i in range(0, len(A)):
            if i <= 0:
                continue
            if direction == 0:
                if A[i] > A[i-1]:
                    direction = 1 #up
                    continue
            if direction == 1:
                if A[i] > A[i-1]:
                    continue
                if A[i] < A[i-1]:
                    direction = 2
                    continue
            if direction == 2:
                if A[i] < A[i-1]:
                    continue
            return False
        return direction == 2