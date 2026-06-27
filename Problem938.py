# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: Optional[TreeNode]
        :type low: int
        :type high: int
        :rtype: int
        """
        
        
        
        def visiter(root,low,high):
            visited =[False]
            stack =[root]
            result =[]
            while stack:
                curr , visit = stack.pop() , visited.pop()
                if curr:
                    if visit:
                        result.append(curr.val)
                    else :
                        stack.append(curr)
                        visited.append(True)
                        stack.append(curr.right)
                        visited.append(False)
                        stack.append(curr.left)
                        visited.append(False)
            sum =0
            for i in result:
                if i!=None: 
                    if i>=low and i<=high:
                        sum += i

            return sum 
        


        def rootsetter(root, low, high):
            if root is None:
                return 0

            if low < root.val and high < root.val:
                return rootsetter(root.left, low, high)

            elif low > root.val and high > root.val:
                return rootsetter(root.right, low, high)

            else:
                return visiter(root, low, high)

        s = rootsetter(root, low, high)
        return s

        
        
        