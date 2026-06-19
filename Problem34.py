class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = 0
        r = len(nums)-1
        if len(nums)==1 and nums[0] == target:
                return [0,0]
        while l<r:
            
            if nums[l]<target:
                l+=1
            if nums[r]>target:
                r=r-1
            if nums[l]==target and nums[r]==target:
                return [l,r]

        return [-1,-1]