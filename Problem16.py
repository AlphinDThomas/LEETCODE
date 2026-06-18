class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        minidiff = 99999999999
        for i,a in enumerate(nums):
            if i>0 and a == nums[i-1]:
                continue

            l,r = i+1,len(nums)-1
            
            while l<r:
                sum = nums[i]+nums[r]+nums[l]
                if sum<target:
                    l+=1
                elif sum>target:
                    r-=1
                else:
                    return sum
                diff = abs(target-sum)
                if minidiff>diff:
                    minidiff = diff
                    result =sum
        return result        