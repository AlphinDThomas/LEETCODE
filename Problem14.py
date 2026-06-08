class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        substring=""
        k=0
        while True:
            if k>=len(strs[0]):
                return substring
            ch = strs[0][k]
            
            for j in strs:
                if k>=len(j):
                    return substring
                if j[k]!=ch:
                    return substring
            substring = substring + ch
            k = k+1