from typing import List, Optional
from heapq import *


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        cur = ListNode()
        cur.next = head
        front = cur.next

        while front:
            cur = front.next
            if cur:
                front.val, cur.val = cur.val, front.val
                front = cur.next
            else:
                front = None

        return head

if __name__ == "__main__":

    n = list(map(int,input("请输入n:").split()))
    n.reverse()
    head = None
    for i in n:
        dummy = ListNode(i)
        dummy.next = head
        head = dummy

    dummy = head
    while dummy:
        print(dummy.val, end='->')
        dummy = dummy.next
    print()

    sol = Solution()
    l = sol.swapPairs(head)

    while l:
        print(l.val, end='->')
        l = l.next
