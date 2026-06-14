# Definition for singly-linked list.
class ListNode(object):
      def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        temp = head
        list1=[]
        while temp!=None:
            list1.append(temp.val)
            temp = temp.next

        list2 = list(set(list1))
        aman = ListNode(0)
        curr = aman
        i=0
        list2.sort()
        for i in range(len(list2)):
            curr.next = ListNode(list2[i])
            curr = curr.next

        dummy = aman
        return dummy.next