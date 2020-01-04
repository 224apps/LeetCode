class Solutions:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            sum = nums[i] + nums[j]
            if sum == target:
                return [i,j]
    
    def main():
        nums [2,7,11,15]
        twoSum(nums, 9)


