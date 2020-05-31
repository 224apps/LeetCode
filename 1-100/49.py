'''
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
'''
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ht ={}
        
        for word in strs:
            
            key = "".join(sorted(word))
            if key in ht:
                ht[key].append(word)
            else:
                ht[key] = [word]
        return list(ht.values())


# class Solution(object):
#     def groupAnagrams(self, strs):
#         """
#         :type strs: List[str]
#         :rtype: List[List[str]]
#        """
#         result = []
#         ht = {}

#         for s in strs:
#             key = findHash(s)
#             if key in ht:
#              ht[hey].append(s)
        
#         for p in ht.values():
#             result.append(p)
#         return result





















# class Solution:
#     def groupAnagrams(self, strs):
#         grouped = {}

#         for word in strs:
#             key = "".join(sorted(word))
#             if key in grouped :
#                 grouped[key].append(word)
#             else:
#                 grouped[key] = [word]
#         return grouped.values()

