'''
Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.

A string is represented by an array if the array elements concatenated in order forms the string.

 

Example 1:

Input: word1 = ["ab", "c"], word2 = ["a", "bc"]
Output: true
Explanation:
word1 represents string "ab" + "c" -> "abc"
word2 represents string "a" + "bc" -> "abc"
The strings are the same, so return true.
Example 2:

Input: word1 = ["a", "cb"], word2 = ["ab", "c"]
Output: false
Example 3:

Input: word1  = ["abc", "d", "defg"], word2 = ["abcddefg"]
Output: true
'''
#Solution1

class Solution:

    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return "".join(word1) == "".join(word2)

#Solution2
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        list1 = []
        list2 = []
        
        for s in word1:
            for c in s:
                list1.append(c)
        
        for s in word2:
            for c in s:
                list2.append(c)
                
        if len(list1) != len(list2):
            return False
        for i in range(len(list1)):
            if list1[i] != list2[i]:
                return False
        return True