class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        substring = ""
        for i in range(len(digits)):
            substring = substring+str(digits[i])
        
        n = int(substring)+1
        list1=[]
        i=0
        while n>0:
            list1.append(n%10)
            n =n//10
        list1 = list1[::-1]
        return list1