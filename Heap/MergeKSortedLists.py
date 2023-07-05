# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeKLists(lists):
    def merge2Lists(l1, l2):
        res = ListNode()
        head = res

        while l1 and l2:
            if l1.val < l2.val:
                res.next = ListNode(l1.val)
                l1 = l1.next
            else:
                res.next = ListNode(l2.val)
                l2 = l2.next
            res = res.next

        if l1 and not l2:
            res.next = l1
        elif l2 and not l1:
            res.next = l2

        return head

    if not lists or len(lists) == 0:
        return None

    while len(lists) > 1:
        merged = []
        for i in range(0, len(lists), 2):
            j = i + 1
            l1 = lists[i]
            l2 = lists[j] if j < len(lists) else None
            merged.append(merge2Lists(l1, l2))
        lists = merged

    return lists[0]
