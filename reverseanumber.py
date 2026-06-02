class Solution(object):
    def reverse(self, x):
        rev =0
        if x >0:
            while x>0:
                digit = x%10
                rev = rev *10 +digit
                x  = x//10
            if rev < -2**31 or rev > 2**31 - 1:
                return 0
            return rev    
        else : 
            y = -x
            while y>0:
                digit = y%10
                rev = rev *10 +digit
                y = y//10
                if rev < -2**31 or rev > 2**31 - 1:
                    return 0
            return -rev
