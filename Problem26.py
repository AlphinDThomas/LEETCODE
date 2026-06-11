class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        aman = list(set(nums))
        for i in range(len(nums)):
            nums[i]= "_"
        for i in range(len(aman)):
            nums[i]=aman[i]
        nums = nums.sort()
        return len(aman)