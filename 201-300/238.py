class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        if not nums:
            return []

        dp = [1] * len(nums)
        cumulativeProduct = 1
        
        #multiply from the right
        for i in range(1, len(nums)):
            dp[i] = dp[i-1] * nums[i -1]
            cumulativeProduct = cumulativeProduct * dp[i]
            
        cumulativeProduct = 1
        
        #multiply from the left
        for i in range(len(nums) - 1, -1, -1):
            dp[i] = dp[i] * cumulativeProduct 
            cumulativeProduct = cumulativeProduct * nums[i]
            
        return dp
