class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        
        p = root.right
        q = root.left
        def check(p,q):
            if not p and not q:
                return True

            if not p or not q:
                return False

            if p.val != q.val:
                return False

            return check(p.left , q.right) and check(p.right,q.left)
        return check(p,q)

#######################OR#######################

"""class Solution(object):
    def isSymmetric(self, root):
        
        :type root: Optional[TreeNode]
        :rtype: bool
        
        stack1=[root.right]
        stack2=[root.left]
        while stack1 and stack2:
            curr1=stack1.pop()
            curr2=stack2.pop()
            if not curr1 and not curr2:
                continue
            if not curr1 or not curr2:
                return False
            if curr1.val!=curr2.val:
                return False
            stack1.append(curr1.right)
            stack1.append(curr1.left)
            stack2.append(curr2.left)
            stack2.append(curr2.right)
        return True"""