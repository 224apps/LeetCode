
class Solution:
    def longestPalindrome(self, s):
        largestPalindrome = ""
        for i in range(len(s)):
            palindromeOdd = self.longestPalindromeAtIndex(s, i, i)
            palindromeEven = self.longestPalindromeAtIndex(s,i, i + 1)

            largerPalindrome = palindromeOdd if len(palindromeOdd) > len(palindromeEven) else palindromeEven
            largestPalindrome = largerPalindrome if len(largestPalindrome) >= len(largerPalindrome) else largerPalindrome
        return largestPalindrome

    
    def longestPalindromeAtIndex( self, s, left, right):
        leftIndex = 0
        rightIndex = 0

        while left >= 0 and right < len(s):
            if s[left] == s[right]:
                leftIndex = left
                rightIndex = right
            else:
                break
                left -= 1
                right += 1
        return s[ leftIndex: rightIndex]



        