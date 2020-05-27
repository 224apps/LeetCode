class Solution:
    def findMin(self, nums):
        if len(nums) == 1:
            return nums[0]
        left = 0
        right = len(nums) - 1

        if nums[0] < nums[right]:
            return nums[0]

        while left < right:
            mid = (left + right) // 2
            midVal = nums[mid]
            rightMidVal = nums[mid + 1]
            leftMidVal = nums[mid - 1]
            if midVal > rightMidVal:
                return rightMidVal
            if leftMidVal > midVal:
                return midVal
            if midVal > nums[0]:
                left  = mid + 1
            else:
                right =  mid - 1
            

