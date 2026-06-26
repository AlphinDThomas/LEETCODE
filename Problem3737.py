class Solution(object):
    def countMajoritySubarrays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        c =0
        for i in range(len(nums)):
            targetcounter=0
            for j in range(i,len(nums)):
                if nums[j]==target:
                    targetcounter+=1
                l = j-i+1
                if targetcounter > l//2:
                    c+=1
                    
        return c