'''
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
'''

class Solution(object):

    def solution(self, nums, ans, curr, index):
        if index > len(nums):
            return
        ans.append(curr[:])
        for i in range(index, len(nums)):
            if (nums[i] not in curr):
                curr.append(nums[i])
                self.solution(nums, ans, curr, i)
                curr.pop()
        return 

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []

        curr = []
        self.solution(nums, ans, curr,0)
        return ans
    


        