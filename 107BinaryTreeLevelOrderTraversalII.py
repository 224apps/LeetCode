# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        self.helper(root, 0, res)
        return res[::-1]
    
        
    def helper(self, node, depth, res):
        if not node:
            return
        if len(res) <= depth:
            res.append([])
        res[depth].append(node.val)
        self.helper(node.left, depth+1, res)
        self.helper(node.right, depth+1, res)