class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = {}
        for num in nums :
            if num in counter:
                counter[num]+=1
            else:
                counter[num]=1
            
        for num in counter:
            if counter[num]==1:
                return num

#OR 
#class Solution(object):
    #def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #seen = set()
        #for num in nums :
            #if num in seen:
                #seen.remove(num)
            #else:
                #seen.add(num)
            
        #element = seen.pop()
        #return element