# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        carry = 0
        returnable_listnode = ListNode(0)
        curr = returnable_listnode
        alist=[]

        while (l1 or l2 or carry):
            value_1 = l1.val if l1 else 0
            value_2 = l2.val if l2 else 0

            curr.next = ListNode((value_1+value_2+carry)%10)
            carry = (value_1+value_2+carry)//10

            curr=curr.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return returnable_listnode.next

        