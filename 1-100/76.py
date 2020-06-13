'''
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
Note:

If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.
'''
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        len1 = len(s)
        len2 = len(t)


        if len1 < len2:
            return ""

        hashPat  = {}
        hashStr = {}

        for i in range(0, len2):
            if (hashPat.get(t[i]) is None):
                hashPat[t[i]] = 0
            hashPat[t[i]] += 1
        count = 0
        left = 0
        startIndex = -1
        minLen =  float('inf')

        for right in range(0, len1):
            if (hashStr.get(s[right]) is None):
                hashStr[s[right]] = 0
            hashStr[s[right]] += 1

            if  (hashStr.get(s[right]) <= hashPat.get(s[right])):
                count += 1
            if (count == len2):
                while (hashStr.get(s[left] > hashPat.get(s[left]))):
                    hashStr[s[left]] -= 1
                    left += 1
            windowLen = right- left + 1
            if minLen > windowLen:
                minLen = windowLen
                startIndex =  left
        if startIndex == -1 :
            return ""
        return s[startIndex: startIndex + minLen]





