# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        list1=[]
        temp = head
        while temp!=None:
            list1.append(temp.val)
            temp = temp.next
        list1 = list1[::-1]
        sum=0
        for i in range(len(list1)):
            sum += list1[i] *  2**i
        return sum

        