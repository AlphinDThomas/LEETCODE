class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        num3 = nums1 + nums2
        num3.sort()
        lenofnum3 = len(num3)
        if lenofnum3%2 == 1:
            count = lenofnum3//2 +1
            return float(num3[count-1])
        else:
            count = lenofnum3//2
            sum1 = num3[count-1]+num3[count]
            sum1 = sum1/2.0
            return sum1

        
            
        