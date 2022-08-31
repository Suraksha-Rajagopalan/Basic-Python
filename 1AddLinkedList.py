# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2, c=0):
        sum = l1.val + l2.val
        carry = int(sum / 10)

        l3 = ListNode(sum % 10)
        p1 = l1.next
        p2 = l2.next
        p3 = l3
        while(p1 != None or p2 != None):
            sum = carry + (p1.val if p1 else 0) + (p2.val if p2 else 0)
            carry = int(sum/10)
            p3.next = ListNode(sum % 10)
            p3 = p3.next
            p1 = p1.next if p1 else None
            p2 = p2.next if p2 else None

        if(carry > 0):
            p3.next = ListNode(carry)

        return l3


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = Solution().addTwoNumbers(l1, l2)
while result:
    print(result.val)
    result = result.next
