class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        if not nums: return 0
        self.count, self.best =  len(nums), 0
        memo = {}
        for i in range(len(nums)):
            if len(nums) - i < self.best: break
            self.rFindSeq(nums, i, 1, memo)
        return self.count
    def rFindSeq(self, nums, left, count, memo):
        c, best = 1, 1
        for i in range(left, len(nums)):
            if nums[i] > nums[left]:
                if i not in memo:
                    memo[i] = self.rFindSeq(nums, i,  1, memo)
                if count + memo[i][0] > best:
                    c = memo[i][1]
                    best = count + memo[i][0]
                elif count + memo[i][0] == best: 
                    c +=  memo[i][1]
        if best > self.best:
            self.best = best
            self.count = c
        elif best == self.best:
            self.count += c
        return (best, c)