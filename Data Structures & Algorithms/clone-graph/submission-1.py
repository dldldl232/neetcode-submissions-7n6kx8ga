"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
# BFS version

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        old_to_new = {node: Node(node.val)}
        queue = deque([node]) # create a double sided queue

        while queue:
            curr = queue.popleft()

            for neighbor in curr.neighbors:
                # if not cloned
                if neighbor not in old_to_new:
                    # create clone and add to map
                    old_to_new[neighbor] = Node(neighbor.val)
                    # add original to queue to mark as visited
                    queue.append(neighbor)

                old_to_new[curr].neighbors.append(old_to_new[neighbor])
            
        return old_to_new[node]

        