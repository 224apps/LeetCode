class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.accumulativeSumCache = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.accumulativeSumCache[i + 1] += self.accumulativeSumCache[i] + nums[i]
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.accumulativeSumCache[j + 1] - self.accumulativeSumCache[i]