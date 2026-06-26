# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#https://www.youtube.com/watch?v=QhszUQhGGlA 
#watch in case of doubt

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        stack = [root]
        visited = [False]
        result = []
        while stack:
            curr = stack.pop()
            visit = visited.pop()
            if curr:
                if visit:
                    result.append(curr.val)
                else:
                    stack.append(curr)
                    visited.append(True)
                    stack.append(curr.right)
                    visited.append(False)
                    stack.append(curr.left)
                    visited.append(False)
        return result