class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        substring=""
        s=s.lower()
        for i in s:
            if i.isalnum():
                substring +=i
        return substring == substring[::-1]