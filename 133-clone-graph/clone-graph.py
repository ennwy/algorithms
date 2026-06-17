"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = {}

        def dfs(node) -> node:
            if not node:
                return None

            if node in visited:
                return visited[node]
            
            clone = Node(node.val)
            visited[node] = clone
            neighbors = []

            for neighbor in node.neighbors:
                neighbor_clone = dfs(neighbor)
                clone.neighbors.append(neighbor_clone)

            return clone
        
        return dfs(node)