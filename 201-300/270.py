'''
Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

Note:

Given target value is a floating point.
You are guaranteed to have only one unique value in the BST that is closest to the target.
Example:

Input: root = [4,2,5,1,3], target = 3.714286

    4
   / \
  2   5
 / \
1   3

Output: 4
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        
        def helper(node):
            nonlocal min_dis, res
            if not node:
                return
            
            if abs(node.val - target) < min_dis:
                min_dis =  abs(node.val - target)
                res = node.val
            
            if node.val < target:
                helper(node.right)
            else:
                helper(node.left)
                
                
        min_dis = sys.maxsize
        res = 0
        helper(root)
        
        return res
