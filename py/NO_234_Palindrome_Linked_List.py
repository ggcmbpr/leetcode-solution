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
        copy=[]
        while head is not None:
            copy.append(head.val)
            head = head.next

        for i in range(len(copy)):
            if copy[i] == copy[len(copy)-1-i]:
                if i <= len(copy)-1-i:
                    continue
                else:
                    break
            else:
                return False

        return True

"""
while writeing code, there are a few corner cases not clear. like empty, just single digit in the list, or [1,2,1].
"""
