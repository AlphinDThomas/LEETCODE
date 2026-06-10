#in this problem leetcode explicitly says edit the list named "nums" which is passed as input list
#nums is checked by leetcode even though it is not returned therefore nums itself should be modified accordingly

class Solution(object):
    def removeElement(self, nums, val):
        list1=[]
        for i in range(len(nums)):
            if nums[i]!=val:
                list1.append(nums[i])
        
        for i in range (len(list1)):
            nums[i] = list1[i]
        return len(list1) 