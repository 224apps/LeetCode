'''
You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.

 

Example 1:

Input:
  s = "barfoothefoobarman",
  words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.
Example 2:

Input:
  s = "wordgoodgoodgoodbestword",
  words = ["word","good","best","word"]
Output: []
'''
class Solution:
    def findSubstring(self, s, words):

        if len(words) == 0: return []
        wordsDict = {}
        for word in words:  # Count the number of occurrences of each word
            if word not in wordsDict:
                wordsDict[word] = 1
            else:
                wordsDict[word] += 1
       # n, m, k respectively, the length of the string, the length of the word, the number of words
        n, m, k = len(s), len(words[0]), len(words)  
        res = []

        for i in range(n - m * k + 1):  # Select an interval or window
            j = 0
            cur_dict = {}

            while j < k:
                word = s[i + m * j:i + m * j + m]  # 
                if word not in wordsDict:  # appears a word that does not exist, directly end this interval
                    break
                if word not in cur_dict:
                    cur_dict[word] = 1
                else:
                    cur_dict[word] += 1
                if cur_dict[word] > wordsDict[word]:  # A word is greater than necessary, then directly end this interval
                    break
                j += 1  # 

            print(j)
            if j == k: res.append(i)  # Record starting position

        return res