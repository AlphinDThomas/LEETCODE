#Singly linked list pallindrome checking
#concept arr = arr[::-1]
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        current = head
        arr=[]
        while current !=None:
            arr.append(current.val)
            current = current.next
        arr1 = arr[::-1]
        if arr == arr1:
            return True
        else : 
            return False
        
        