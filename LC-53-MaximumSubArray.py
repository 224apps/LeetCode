class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: 

            return 0

        result = nums[0]
        for i in range(1, len(nums)):
            nums[i] = max( nums[i], nums[i] + nums[i-1])
            result = max( result, nums[i])
        return result


print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) == 6)