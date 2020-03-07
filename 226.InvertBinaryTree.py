# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.helper(root)
        return root

    def helper(self, node):
        if not node:
            return
        node.left, node.right = node.right, node.left

        self.helper(node.left)
        self.helper(node.right)
        