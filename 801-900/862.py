'''
Return the length of the shortest, non-empty, contiguous subarray of A with sum at least K.

If there is no non-empty subarray with sum at least K, return -1.

 

Example 1:

Input: A = [1], K = 1
Output: 1
Example 2:

Input: A = [1,2], K = 4
Output: -1
Example 3:

Input: A = [2,-1,2], K = 3
Output: 3
 

Note:

1 <= A.length <= 50000
-10 ^ 5 <= A[i] <= 10 ^ 5
1 <= K <= 10 ^ 9

'''
class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        
        
        queue = collections.deque()
        
        n = len(A)
        sums = [0] * (n+1)
        
        res = sys.maxsize
        
        for i in range(1, n+1):
            sums[i] = A[i-1] + sums[i-1]
        
        for right, s in enumerate(sums):
            while queue and s <= sums[queue[-1]]:
                queue.pop()
            while queue and (s - sums[queue[0]]) >= K:
                res = min(res, right - queue.popleft())
                
            queue.append(right)
            
        return res if res != sys.maxsize else -1