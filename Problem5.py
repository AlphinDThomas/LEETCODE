#longest pallindromic substring
class Solution(object):
    def longestPalindrome(self, s):
        longest = ""
        for i in range (len(s)):
            for j in range(i+1, len(s)+1):
                substring= s[i:j]
                if substring == substring[::-1]:
                    if len(longest) < len(substring):
                        longest = substring 
        return longest