# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        stack = []
        
        if root != None:
            stack.append(root)
            while len(stack) != 0:
                temp = stack.pop()
                res.append(temp.val)
                if temp.right != None:
                    stack.append(temp.right)
                if temp.left != None:
                    stack.append(temp.left)
        return res