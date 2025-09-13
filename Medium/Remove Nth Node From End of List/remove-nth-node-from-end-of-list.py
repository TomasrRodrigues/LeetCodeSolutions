class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        returnable = ListNode(0)
        returnable.next = head
        curr = head
        prev = returnable
        if n > 1:
            for i in range(n-1):
                curr = curr.next
        
        while curr.next:
            curr = curr.next
            prev = prev.next
        
        skip = prev.next.next
        prev.next = skip
        return returnable.next
        