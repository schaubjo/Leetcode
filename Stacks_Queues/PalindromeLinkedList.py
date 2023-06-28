class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def isPalindrome(head):
    # find middle of linked list (slow)
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    # reverse second half of list
    prev = None
    curr = slow
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next

    # check palindrome
    l, r = head, prev
    while r:
        if l.val != r.val:
            return False
        else:
            l, r = l.next, r.next

    return True