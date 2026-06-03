class ListNode(object):
    def __init__(self,val=0,next=None):
        self.val =val
        self.next = next
class Solution(object):

    def removeNthFromEnd(self,head,n):
        count =0
        curr = head
        while curr != None:
            count = count + 1
            curr = curr.next
        current = head
        position = count - n
        if position ==0:
            self.head = head.next
            return self.head
        temp = current
        for i in range (position):
            temp = current
            current = current.next
        temp.next = current.next
        return head
        
        