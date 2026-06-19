class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        count ={}
        for i in nums:
                if i in count:
                    count[i]=count[i]+1
                else:
                    count[i]=1
            
        index =0
        for i in [0,1,2]:
            if i in count:
                for j in range(count[i]):
                    nums[index]=i
                    index+=1
