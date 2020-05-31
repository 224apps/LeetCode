'''
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
'''

# class Solution(object):
#     def searchRange(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         for i in range(len(nums)):
#             if nums[i] == target:
#                 leftIndex = i
#                 break
#         else:
#             return [-1, -1]
        
#         for j in range(len(nums) - 1, -1,-1):
#             if nums[j] == target:
#                 rightIndex = j
#                 break
#         return [ leftIndex, rightIndex]




class Solution(object):
  
  
    def getLeftPos(self, nums, target):
      left = 0
      right = len(nums) - 1
      while left <= right:
        mid =  left + (right - left) // 2
        if target == nums[mid]:
          if (mid - 1 >= 0 and nums[mid - 1] != target or mid == 0):
            return mid
          right = mid - 1
        elif nums[mid] > target:
          right = mid - 1
        else:
          left = mid + 1
      return -1
      
    def getRightPos(self, nums, target):
      left = 0
      right = len(nums) - 1
      while left <= right:
        mid =  left + (right - left) // 2
        if target == nums[mid]:
          if (mid + 1 < len(nums) and nums[mid + 1] != target or mid == len(nums)-1):
            return mid
          left = mid + 1 
        elif nums[mid] > target:
          right = mid - 1
        else:
          left = mid + 1
      return -1
      
      
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = self.getLeftPos(nums, target)
        right = self.getRightPos(nums, target)
        return [left, right]
        
    
