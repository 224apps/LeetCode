'''
Given an array of integers nums, sort the array in ascending order.
Example 1:

Input: nums = [5,2,3,1]
Output: [1,2,3,5]
Example 2:

Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]
 

Constraints:

1 <= nums.length <= 50000
-50000 <= nums[i] <= 50000
'''
class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return self.mergeSort(nums)
    
    def mergeSort(self, nums):
        if len(nums)<= 1:
            return nums
        mid = len(nums) / 2
        left = self.mergeSort(nums[:mid])
        right = self.mergeSort(nums[mid:])

        block = []
        l = r = 0

        while l < len(left) and r < len(right):
            if left[l] < right[r]:
                block.append(left[l])
                l += 1
            else:
                block.append(right[r])
                r += 1
        if l < len(left):
            block += left[l:]
        elif r < len(right):
            block += right[r:]
        return block
    