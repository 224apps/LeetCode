'''
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
'''
class Solution:
    def doPermuteUnique(self, num_list):
        if 1 == len(num_list):
            return [ num_list ]
        res_list = [ ]
        for i in range(0, len(num_list)):
            if i > 0 and num_list[0] == num_list[i]:
                continue
            num_list[0], num_list[i] = num_list[i], num_list[0]
            sub_res_list = self.doPermuteUnique(num_list[1:])
            list_head = [ num_list[0] ]
            new_list = [ list_head + list for list in sub_res_list]
            res_list.extend(new_list)
        return res_list

    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        return self.doPermuteUnique(nums)