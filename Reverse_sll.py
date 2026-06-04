class Solution(object):
    def reverseList(self, head):
        current = head
        arr =[]
        while current!= None:
            arr.append(current.val)
            current = current.next
        arr= arr[::-1]
        temp = head
        count=0
        while temp!= None:
            count = count +1
            temp = temp.next
        temp1 = head
        for i in range (count):
            temp1.val = arr[i]
            temp1 = temp1.next
        return head