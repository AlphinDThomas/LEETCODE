class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result =set()
        for i in nums:
            result.add(i)
        final =[]
        for i in result:
            final.append(i)
        if len(final)<3:
            return max(final)
        for i in range(2):
            m = max(final)
            final.remove(m)

        return max(final)