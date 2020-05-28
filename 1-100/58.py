class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        localCount = 0
        
        for i in range(len(s)):
            if s[i] == ' ':
                localCount = 0
            else:
                localCount += 1
                count = localCount
        return count