# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        temp1 = headA
        temp2 = headB

        visited = set()
        while temp1!=None:
            visited.add(temp1)
            temp1 = temp1.next
        while temp2!=None:
            if temp2 in visited:
                return temp2
            temp2 = temp2.next