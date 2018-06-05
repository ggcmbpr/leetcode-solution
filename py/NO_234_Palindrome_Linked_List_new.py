# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(2)
head.next.next.next = ListNode(1)
"""
while head is not None:
    print head.val
    head = head.next
"""

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        #find middle pointer
        slow=fast=head
        while fast is not None and fast.next is not None:
            if fast.next.next is None:
                fast = fast.next
                temp = slow.next
                slow.next = None
                slow = temp
            else:
                fast = fast.next.next
                slow = slow.next

        slow = self.reverse(slow)

        while head is not None:
            if head.val == slow.val:
                head = head.next
                slow = slow.next
                continue
            else:
                return False

        return True



    # reverse singly linked list
    def reverse(self,head):
        if head is not None:
            next = head.next
            head.next = None
            while next is not None:
                temp = next.next
                next.next = head
                head = next
                next = temp

        return head

print Solution().isPalindrome(head)

"""good solution from leetcode best time"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        rev = None
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            rev, slow.next, slow = slow, rev, slow.next
        # CHECK odd
        if fast:
            slow = slow.next
        while slow:
            if slow.val != rev.val:
                return False
            slow, rev = slow.next, rev.next
        return True
