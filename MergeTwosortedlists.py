# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        list3 = []
        current1 = list1
        current2 = list2
        while current1!=None:
            list3.append(current1.val)
            current1 = current1.next
        while current2!= None:
            list3.append(current2.val)
            current2 = current2.next
        list3.sort()
        Sortedmerge = ListNode(0)
        temp = Sortedmerge
        
        for i in list3:
            temp.next = ListNode(i)
            temp = temp.next
        return Sortedmerge.next

