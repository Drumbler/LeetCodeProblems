from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     prev = None
    #     curr = head
    #     while curr:
    #         nxt = curr.next
    #         curr.next = prev
    #         prev = curr
    #         curr = nxt
    #     return prev

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tmp = None
        p = head
        while p:
            tmp = ListNode(p.val, tmp)
            p = p.next
        return tmp


def printList(head):
    temp = head
    while temp:
        print(temp.val)
        temp = temp.next


s = Solution()
s.head = ListNode(1)
s.head.next = ListNode(2)
s.head.next.next = ListNode(3)
s.head.next.next.next = ListNode(4)

revers = s.reverseList(s.head)
printList(revers)
