# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        root = TreeNode(preorder[0])
        stack = [root]
        for index in range(1, len(preorder)):
            newNode = TreeNode(preorder[index])
            if newNode.val < stack[-1].val:
                stack[-1].left = newNode
            else:
                parent = None
                while stack and newNode.val > stack[-1].val:
                    parent = stack.pop()
                parent.right = newNode
            stack.append(newNode)
        return root