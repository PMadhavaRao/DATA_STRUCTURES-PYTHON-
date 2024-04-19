# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy=ListNode(-1)
        curr=dummy
        carry=0
        while l1 is not None or l2 is not None:
            summ=carry
            if(l1):
                summ+=l1.val
            if(l2):
                summ+=l2.val
            curr.next=ListNode(summ%10)
            carry=summ//10
            curr=curr.next
            if(l1):
                l1=l1.next
            if(l2):
                l2=l2.next
        
        if (carry):
            curr.next=ListNode(carry)
        return dummy.next

