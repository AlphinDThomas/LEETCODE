# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        list1=[]
        def dfs(node,path):
            if not node :
                return 
        
            if path =="":
                path = str(node.val)
            else:
                path = path + "->" + str(node.val)
            
            if not node.left and not node.right:
                list1.append(path)
                return list1
            
            dfs(node.left, path)
            dfs(node.right,path)
            return list1
        
        return dfs(root,"")



        
        



        