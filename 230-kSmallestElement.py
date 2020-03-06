class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        data = []
        #Helper function
        def traverse(node):
            if node.left:
                traverse(node.left)
            data.append(node.val)
            if node.right:
                traverse(node.right)
                
        traverse(root)
        return data[k-1]