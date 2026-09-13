class Solution:
    def reverseKGroup(self, head, k):
        node = head

        for i in range(k):
            if node is None:
                return head
            node = node.next

        prev = None
        curr = head

        for i in range(k):
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        head.next = self.reverseKGroup(curr, k)

        return prev