class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack =[]
        opening = ["(","[","{"]
        for char in s:
            if char in opening:
                stack.append(char)
            else:
                if len(stack)==0:
                    return False
                elif char == ")" and stack[-1]=="(" or char == "]" and stack[-1]=="[" or char == "}" and stack[-1]=="{":
                    stack.pop()
        
                else:
                    return False
        if len(stack)!=0:
            return False
        else: 
            return True