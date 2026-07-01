# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def checker(root):
            if not root:
                return 0
            
            if not root.left and not root.right:
                return 1
            
            if not root.left:
                return 1+ checker(root.right)
            if not root.right:
                return 1 + checker(root.left)

            return 1 + min(checker(root.left), checker(root.right))
        return checker(root)
