class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = {}
        m = len(nums)/2
        for i in nums:
            if i in count:
                count[i]+=1
            elif i not in count:
                count[i]=1
            if count[i]>m:
                return i
                
#OR

#nums.sort()
        #return nums[len(nums)//2]