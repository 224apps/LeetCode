'''
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
'''
import copy 
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        def permuteHelper(start):
            if start == len(nums):
                res.append(copy.copy(nums))
            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]
                permuteHelper(start+1)
                nums[start], nums[i] = nums[i], nums[start]
        permuteHelper(0)
        return res

        
nums =[1,2,3,4,5]
print(Solution().permute(nums))
        
        
        