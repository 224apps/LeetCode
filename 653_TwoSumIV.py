class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        if not root:
            return 
        hashSet = set()
       # hashMap = {}
        queue = [root]
        while queue:
            node = queue.pop(0)
            if (k - node.val)  in hashSet:
                return True
            hashSet.add(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return False
