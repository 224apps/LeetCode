# class Solutions:
#     def twoSum(self, nums, target):
#         for i in range(len(nums)):
#         for j in range(i+1, len(nums)):
#             sum = nums[i] + nums[j]
#             if sum == target:
#                 return [i,j]
    
#     def main():
#         nums [2,7,11,15]  
#         twoSum(nums, 9)



# class Solution(object):
#     def twoSum(self, numbers, target):
#         """
#         :type numbers: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         begin = 0
#         end = len(numbers) -1
        
#         while begin < end:
#             curr = numbers[begin] + numbers[end]
#             if curr == target:
#                 return [ begin + 1, end + 1]
#             elif curr < target:
#                 begin += 1
#             else:
#                 end -= 1
        
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ht = {}
        n = len(nums)
        for i in range(0, n):
          val = target - nums[i]
          if val in ht:
            return [ ht[val], i]
          ht[nums[i]] = i