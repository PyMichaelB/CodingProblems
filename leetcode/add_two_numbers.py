# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        current = ListNode()
        l3 = current
        carry = 0

        while l1 or l2:
            current.next = ListNode(carry)
            current = current.next

            current.val += l1.val if l1 else 0
            current.val += l2.val if l2 else 0

            carry = current.val // 10
            current.val = current.val % 10  # i.e. 28 gives value 8 with carry 2

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        if carry:
            current.next = ListNode(carry)

        return l3.next