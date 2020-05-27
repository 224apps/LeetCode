class Solution:
    def canJump(self, nums):


        # dp_positions = [False] * len(nums)
        
        # dp_positions[0] = True

        # for j in range(1, len(nums)):
        #     for i in range(j):
        #         if dp_positions[i] and i + nums[i]  >= j:
        #             dp_positions[j] = True

        # return dp_positions[-1]


        max_reach = 0

        for current_step in range(len(nums)):
            if current_step > max_reach:
                return False
            
            current_reach = current_step + nums[current_step]
            max_reach = max(max_reach, current_reach)
        return True