class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head ==None:
            return head
        p1= head
        p2 = head.next
        while p2!=None:
            temp = p1.val
            p1.val = p2.val
            p2.val = temp

            if p2.next!=None:
                p1 = p2.next
            else:
                break
            
            if p1.next!=None:
                p2 = p1.next
            else :
                break
        
        return head