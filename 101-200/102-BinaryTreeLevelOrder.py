# # Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution(object):
#     def levelOrder(self, root):
#         """
#         :type root: TreeNode
#         :rtype: List[List[int]]
#         """
#         if not root:
#             return []
#         queue = [(root,0)]
#         levelMap = {}
        
#         while queue:
#             node, level = queue.pop(0)
#             if node.left:
#                 queue.append((node.left, level + 1))
#             if node.right:
#                 queue.append((node.right, level + 1))
#             if level in levelMap:
#                 levelMap[level].append(node.val)
#             else:
#                 levelMap[level] = [node.val]
#         result = []
#         for key, value in levelMap.iteritems():
#         	result.append(value)
#         return result


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res= []
        self.helper(root, 0, res)

    def helper(self, node, depth, res):
        if not  node:
            return
        if len(res) <= depth:
            res.append([])
        res[depth].appen(node.val)
        self.helper(node.left, depth+ 1, res)
        self.helper(node.right, depth+1, res)
        
