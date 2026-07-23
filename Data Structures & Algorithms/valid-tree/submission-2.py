class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # A tree with n nodes must have exactly n - 1 edges.
        if len(edges) != n - 1:
            return False

        adj = [[] for _ in range(n)]

        for node1, node2 in edges:
            adj[node1].append(node2)
            adj[node2].append(node1)

        visited = set()
        stack = [0]

        while stack:
            node = stack.pop()

            if node in visited:
                continue

            visited.add(node)

            for neighbor in adj[node]:
                if neighbor not in visited:
                    stack.append(neighbor)

        return len(visited) == n