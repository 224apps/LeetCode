# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        currNode = root
        
        while currNode:
            if currNode.val < p.val and currNode.val < q.val:
                currNode = currNode.right
            elif currNode.val > p.val and currNode.val > q.val:
                currNode = currNode.left
            else:
                return currNode