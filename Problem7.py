class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x<0:
            x = x *-1
            y = x
            rev =0
            while y>0:
                digit = y%10
                rev = rev*10+digit
                y = y//10
            rev = rev*-1
            if rev <-2**31 or rev > 2**31 -1:
                return 0
            return rev
        else:
            y = x
            rev =0
            while y>0:
                digit = y%10
                rev = rev*10+digit
                y = y//10
            if rev <-2**31 or rev > 2**31 -1:
                return 0
            return rev