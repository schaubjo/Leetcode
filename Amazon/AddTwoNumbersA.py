# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1, l2):
    dummy = ListNode()
    res = dummy
    carry = 0
    while l1 or l2 or carry > 0:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        newVal = val1 + val2 + carry
        carry = 1 if newVal > 9 else 0

        res.next = ListNode(newVal % 10, None)
        l1 = l1.next if l1 else l1
        l2 = l2.next if l2 else l2
        res = res.next

    return dummy.next


a3 = ListNode(3)
a2 = ListNode(4, a3)
a1 = ListNode(2, a2)

b3 = ListNode(4)
b2 = ListNode(6, b3)
b1 = ListNode(5, b2)

res = addTwoNumbers(a1, b1)
while res:
    print(res.val)
    res = res.next
