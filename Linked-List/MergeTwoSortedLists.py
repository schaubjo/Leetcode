class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1, list2):
    merged = ListNode()
    res = merged
    while list1 or list2:
        if not list1:
            merged.next = list2
            list2 = list2.next
        elif not list2:
            merged.next = list1
            list1 = list1.next
        elif list1.val < list2.val:
            merged.next = list1
            list1 = list1.next
        else:
            merged.next = list2
            list2 = list2.next
        merged = merged.next
    return res.next


a3 = ListNode(4)
a2 = ListNode(2, a3)
a1 = ListNode(1, a2)

b3 = ListNode(4)
b2 = ListNode(3, b3)
b1 = ListNode(1, b2)

res = mergeTwoLists(a1, b1)
while res:
    print(res.val)
    res = res.next
