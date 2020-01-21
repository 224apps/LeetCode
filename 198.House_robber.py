class Solutions:
    def rob(self, nums):

        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        #max loot for two houses
        max_loot_at_nth_house = max(nums[0], nums[1])


        for i in range(2, len(nums)):
            max_loot_at_nth_house.append(max(nums[i] + max_loot_at_nth_house[i-2], max_loot_at_nth_house[i-1]))
        return max_loot_at_nth_house.pop()
        


