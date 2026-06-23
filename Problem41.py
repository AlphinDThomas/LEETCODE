class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        expected =1
        nums = sorted(set(nums))
        i=0
        for num in nums:
            if num <expected:
                i+=1
            elif num>expected:
                return expected
            else :
                expected+=1
                i+=1
        return expected