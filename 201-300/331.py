# class Solution(object):
#     def isValidSerialization(self, preorder):
#         """
#         :type preorder: str
#         :rtype: bool
#         """
#         p = preorder.split(',')
#         slots = 1
        
#         for node in p:
#             slots -= 1
            
#             if slots < 0:
#                 return False
            
#             if node != "#":
#                 slots += 2
#         return slots == 0
            
class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """

        slots = 1
        for i in range(len(preorder)):
            char = preorder[i]
            if char == ",":
                slots -= 1
            
                if slots < 0:
                    return False
                prevChar = preorder[i-1]
                if prevChar != "#":
                   slots += 2
        if preorder[-1] == "#":
            slots -= 1
        else:
            slots += 1

        return slots == 0
