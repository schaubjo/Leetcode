class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1, l2):
    stack1 = []
    stack2 = []
    while l1:
        stack1.append(l1.val)
        l1 = l1.next
    while l2:
        stack2.append(l2.val)
        l2 = l2.next

    carry = 0
    res = None
    while stack1 or stack2 or carry > 0:
        val1 = stack1.pop() if stack1 else 0
        val2 = stack2.pop() if stack2 else 0

        sum = (val1 + val2 + carry)
        carry = 1 if sum > 9 else 0
        added = ListNode(sum % 10, res)
        res = added

    return res


a4 = ListNode(3)
a3 = ListNode(4, a4)
a2 = ListNode(2, a3)
a1 = ListNode(7, a2)

b3 = ListNode(4)
b2 = ListNode(6, b3)
b1 = ListNode(5, b2)

res = addTwoNumbers(a1, b1)
while res:
    print(res.val)
    res = res.next

c1 = ListNode(5)
d1 = ListNode(5)
x = addTwoNumbers(c1, d1)
while x:
    print(x.val)
    x = x.next
