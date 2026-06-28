# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """

        stack = [root]
        a = root.val
        while stack:
            curr = stack.pop()
            if curr!=None:
                if curr.val!=a:
                    return False
            else :
                continue
            stack.append(curr.left)
            stack.append(curr.right)
        
        return True
      
################################OR#################################

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """

        def checker(node):

            if not node:
                return True

            if node.val!= root.val:
                return False

            return checker(node.right) and checker(node.left)
        
        return checker(root)