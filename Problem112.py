# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """

        def dfs(node,currsum):
            if not node:
                return False
            
            currsum = currsum + node.val
            if not node.left and not node.right:
                if currsum == targetSum:
                    return True
                else :
                    return False

            return dfs(node.left,currsum) or dfs(node.right,currsum)
        return dfs(root,0)