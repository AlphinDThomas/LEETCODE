# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        list1=[]
        temp = head
        while temp!=None:
            list1.append(temp.val)
            temp = temp.next
        
        lent = len(list1)
        
        mid = lent//2
        for i in range(mid):
            head = head.next
        return head
        