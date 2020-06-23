'''
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Example 1:

Input: [1,2,3,1]
Output: true
Example 2:

Input: [1,2,3,4]
Output: false
Example 3:

Input: [1,1,1,3,3,4,3,2,4,2]
Output: true
'''
# # Solution 1
# class Solution(object):
#     def containsDuplicate(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: bool
#         """
#         hashSet = set()
#         if not nums:
#             return False
        
#         for num in nums:
#             if num in hashSet:
#                 return True
#             hashSet.add(num)

#Solution 2

# class Solution(object):
#     def containsDuplicate(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: bool
#         """
#         return True if len(set(nums)) < len(nums) else False


# #Solution 3

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hashSet = {}
        
        for num in nums:
            if num in hashSet:
                return True
            hashSet[num] = 1
        return False
