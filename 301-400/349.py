'''
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Note:

Each element in the result must be unique.
The result can be in any order.
'''

# class Solution(object):
#     def intersection(self, nums1, nums2):
#         """
#         :type nums1: List[int]
#         :type nums2: List[int]
#         :rtype: List[int]
#         """
#         if  not nums1 and  not nums2:
#             return []
#         hashMap = {}
#         res = []
        
#         for num in nums1:
#             if num in hashMap:
#                 hashMap[num] = True
#             else:
#                 hashMap[num] = False
                
#         for num in nums2:
#             if num in hashMap:
#                 hashMap[num] = False
                
#         for key in hashMap:
#             if hashMap[key] == False and key in nums2:
#                 res.append(key)
                
#         return res
            


class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        if  not nums1 and  not nums2:
            return []
        
        return  set(nums1).intersection(set(nums2))