# Definition for singly-linked list.
class ListNode(object):
   def __init__(self, val=0, next=None):
     self.val = val
     self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        temp1 = l1
        temp2 = l2
        list1=[]
        list2=[]
        while temp1!=None:
            list1.append(temp1.val)
            temp1 = temp1.next
        while temp2!=None:
            list2.append(temp2.val)
            temp2 = temp2.next
        
        if len(list1)>len(list2):
            diff = len(list1)-len(list2)
            for i in range(diff):
                list2.append(0)
        elif len(list2)>len(list1):
            diff = len(list2)- len(list1)
            for i in range(diff):
                list1.append(0)
        list1= list1[::-1]
        list2= list2[::-1]
        sum=[]
        for i in range(len(list1)):
            sum.append(list1[i] + list2[i])



        def carryadder(sum):    
            for i in range(len(sum)):
                if sum[i]>=10:
                    carry=1
                    remainder = sum[i]%10
                    sum[i] = remainder
                    if i ==0:
                        sum.insert(0,carry)
                    else:
                        sum[i-1] = sum[i-1]+carry
            for i in range(len(sum)):
                if sum[i]>=10:
                    carryadder(sum)

        carryadder(sum)

        sum = sum[::-1]
        dummy = ListNode(0)
        current = dummy
        for i in range(len(sum)):
            current.next = ListNode(sum[i])
            current = current.next
        return dummy.next