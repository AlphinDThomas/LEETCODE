# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
        result =[]
        arr =[]
        temp = head
        while temp!=None:
            arr.append(temp.val)
            temp = temp.next
        for i in range(len(arr)):
            if i >= left-1 and i<=right-1:
                result.append(arr[i])
        result = result[::-1]
        j=0
        for i in range(len(arr)):
            if i>= left-1 and i<=right-1:
                arr[i]= result[j]
                j+=1
        
        rev = ListNode(0)
        dummy =rev
        for i in range(len(arr)):
            dummy.next = ListNode(arr[i])
            dummy = dummy.next
        
        return rev.next