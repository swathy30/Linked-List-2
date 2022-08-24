class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        mid = self.findmid(head)
        mid_nxt = mid.next
        mid.next = None
        head2 = self.reverse(mid_nxt)
        head1 = head
        return self.mergell(head1,head2)
    
    def findmid(self,head):
        slow = head
        fast = head
        while fast.next!= None and fast.next.next!= None:
            fast = fast.next.next
            slow = slow.next
        return slow
    
    def reverse(self,head):
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
    
    def mergell(self,head1,head2):
        p1 = head1
        p2 = head2
        while p2:
            temp = p1.next
            p1.next = p2
            p2 = p2.next
            p1.next.next = temp
            p1 = temp
        return head1