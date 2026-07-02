# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        result = []
        def checker(root):
            
            if root is None:
                return

            checker(root.left)
            result.append(root.val)
            checker(root.right)
        
        checker(root)

        list2 = list(set(result))
        mini = min(list2)
        list2.remove(mini)
        if not list2:
            return -1
        return min(list2)
        
