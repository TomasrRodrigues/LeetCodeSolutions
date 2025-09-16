# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        returnable = ListNode(0)
        returnable.next = head
        group_prev = returnable

        while True:
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return returnable.next 

            group_next = kth.next

            prev, curr = group_next, group_prev.next
            for _ in range(k):
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            tmp = group_prev.next  
            group_prev.next = prev
            group_prev = tmp