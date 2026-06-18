class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        sum=0
        seen = set()
        while sum!=1:
            sum=0
            while n>0:
                digit=n%10
                sum = sum+digit*digit
                n =n//10
            n = sum
            if sum ==1:
                return True
            else:
                if sum in seen:
                    return False
                seen.add(sum)