# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        stack = [root]
        result = []
        visited = [False]
        while stack:
            curr = stack.pop()
            visit = visited.pop()

            if curr:
                if visit:
                    result.append(curr.val)
                else:
                    stack.append(curr.right)
                    visited.append(False)
                    stack.append(curr)
                    visited.append(True)
                    stack.append(curr.left)
                    visited.append(False)
        return result