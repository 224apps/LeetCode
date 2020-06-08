'''
Given a binary tree, return the postorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [3,2,1]
Follow up: Recursive solution is trivial, could you do it iteratively?
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        answer =  []
        s1 = s2 = []

        s1.append(root)
        while s1:
            elem = s[-1]
            s1.pop()
            s2.append(elem)

            if elem.left:
                s.append(elem.left)
            if elem.right:
                s1.append(elem.right)
        while s2:
            y = s2[-1]
            s2.pop()
            answer.append(y.val)
        return answer