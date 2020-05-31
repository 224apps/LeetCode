'''
Given an array A of integers, return true if and only if it is a valid mountain array.

Recall that A is a mountain array if and only if:

A.length >= 3
There exists some i with 0 < i < A.length - 1 such that:
A[0] < A[1] < ... A[i-1] < A[i]
A[i] > A[i+1] > ... > A[A.length - 1]

Example 1:

Input: [2,1]
Output: false
Example 2:

Input: [3,5,5]
Output: false
Example 3:

Input: [0,3,2,1]
Output: true

Note:
0 <= A.length <= 10000
0 <= A[i] <= 10000 
'''
# class Solution(object):
#     def validMountainArray(self, A):
#         """
#         :type A: List[int]
#         :rtype: bool
#         """
#         direction = 0
        
#         for i in range(0, len(A)):
#             if i <= 0:
#                 continue
#             if direction == 0:
#                 if A[i] > A[i-1]:
#                     direction = 1 #up
#                     continue
#             if direction == 1:
#                 if A[i] > A[i-1]:
#                     continue
#                 if A[i] < A[i-1]:
#                     direction = 2
#                     continue
#             if direction == 2:
#                 if A[i] < A[i-1]:
#                     continue
#             return False
#         return direction == 2


class Solution(object):
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A) <= 3:
            return False
        i = 1
        while(i< len(A) && A[i] > A[i-1]):
            i += 1
        if ( i==1 && i == len(A)):
            return false
        while (i < len(A) && A[i] < A[i-1]):
            i += 1
        return i == len(A)











