# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: List[List[int]]
        """
        result=[]
        
        def dfs(node,path):
            if not node:
                return 
            
            path.append(node.val)
            
            if not node.left and not node.right:
                if sum(path)== targetSum:
                    result.append(list(path))
            
            dfs(node.left,path)
            dfs(node.right,path)
            path.pop()

            return result

        path=[]
        return dfs(root,path)


        