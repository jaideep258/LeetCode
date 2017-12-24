# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if (l1 is None):
            return l2
        elif (l2 is None):
            return l1
        
        newhead,carry,curr= None,0,ListNode(0)
        
        while (l1 and l2):
            sum = l1.val + l2.val + carry
            curr.next = ListNode(sum%10)
            carry = sum/10
            l1,l2,curr = l1.next,l2.next,curr.next
            if (newhead is None):
                newhead = curr
        if l1:
            while l1:
                sum = l1.val + carry
                curr.next = ListNode(sum%10)
                carry = sum/10
                l1,curr = l1.next,curr.next
        if l2:
            while l2:
                sum = l2.val + carry
                curr.next = ListNode(sum%10)
                carry = sum/10
                l2,curr = l2.next,curr.next
        if carry:
            curr.next = ListNode(carry)
         
        return newhead
            
            
