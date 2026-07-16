class TreeNode:
    def __init__(self, value, height):
        self.value = value
        self.height = height
class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount ==0: 
            return 0 
        root = TreeNode(0,0)
        queue = deque([root])
        visited = set()
        visited.add(0)

        while queue:
            currNode = queue.popleft()
            for coin in coins:
                new_sum = currNode.value + coin
                if new_sum == amount:
                    return currNode.height + 1 
                if new_sum < amount and new_sum not in visited:
                    visited.add(new_sum)
                    queue.append(TreeNode(new_sum, currNode.height + 1))
        return -1 