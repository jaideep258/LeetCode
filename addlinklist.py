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
        
        newhead,carry,curr = None,0,ListNode(0)
        
        while (l1 or l2):
            sum = 0
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            sum += carry
            curr.next = ListNode(sum%10)
            carry = sum/10
            curr = curr.next
            if (newhead is None):
                newhead = curr
        if carry:
            curr.next = ListNode(carry)
         
        return newhead
