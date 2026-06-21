class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        result=[]

        for dihh in intervals:
            if not result or result[-1][1] < dihh[0]:
                result.append(dihh)
            else:
                result[-1][1]= max(result[-1][1], dihh[1])
        return result