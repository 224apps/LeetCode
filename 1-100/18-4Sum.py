class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        sumMapping = {}
        for indexI in range(len(nums)-1):
            for indexJ in range(indexI+1, len(nums)):
                currSum = nums[indexI] + nums[indexJ]
                if currSum in sumMapping:
                    sumMapping[currSum].append((indexI, indexJ))
                else:
                    sumMapping[currSum] = [(indexI, indexJ)]
        result = set()
        
        for (key, value) in sumMapping.iteritems():
            diff = target - key
            if diff in sumMapping:
                firstSet = value
                secondSet = sumMapping[diff]
                
                for ( i, j) in firstSet:
                    for (k, l)  in secondSet:
                        fourlet = [i,j,k,l]
                        if len(set(fourlet)) != len(fourlet):
                            continue
                        fourlist = [ nums[i], nums[j], nums[k], nums[l] ] 
                        fourlist.sort()
                        result.add(tuple(fourlist))
        return list(result)