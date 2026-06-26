# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#https://youtu.be/afTpieEZXck?si=v4FyVM3VXnHoxJHI
#Watch in case of doubts

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        result = []
        stack =[]
        curr = root

        while curr!=None or len(stack)!=0:
            if curr!=None:
                result.append(curr.val)
                stack.append(curr.right)
                curr = curr.left
            else:
                curr = stack.pop()
        return result

        