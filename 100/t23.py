from typing import List, Optional
from heapq import *
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        setattr(ListNode, "__lt__", lambda a, b: a.val < b.val)
        pq = [head for head in lists if head]
        heapify(pq)
        dummy = cur = ListNode()
        while pq:
            node = heappop(pq)
            if node.next:
                heappush(pq, node.next)
            cur.next = node
            cur = cur.next
        return dummy.next


if __name__ == "__main__":
    m = int(input("请输入m："))
    l = []
    for j in range(m):
        n = list(map(int,input("请输入n:").split()))
        n.reverse()
        head = None
        for i in n:
            dummy = ListNode(i)
            dummy.next = head
            head = dummy
        l.append(head)
    for dummy in l:
        while dummy:
            print(dummy.val, end='->')
            dummy = dummy.next
        print()
    sol = Solution()
    l = sol.mergeKLists(l)

    while l:
        print(l.val, end='->')
        l = l.next
