class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None:
            return

        nodeList = []
        currNode = head

        while currNode:
            nodeList.append(currNode)
            currNode = currNode.next

        odds = 1
        evens = len(nodeList) - 1
        curr = head

        while odds <= evens:
            # Append the last remaining node.
            curr.next = nodeList[evens]
            curr = curr.next
            evens -= 1

            # If all nodes have now been used, stop.
            if odds > evens:
                break

            # Append the next node from the front.
            curr.next = nodeList[odds]
            curr = curr.next
            odds += 1

        curr.next = None