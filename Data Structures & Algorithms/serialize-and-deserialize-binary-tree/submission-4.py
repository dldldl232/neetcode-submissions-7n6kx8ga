from collections import deque

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "N"

        res = []
        queue = deque([root])

        while queue:
            node = queue.popleft()

            if node is None:
                res.append("N")
            else:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)

        return ",".join(res)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        values = data.split(",")

        if values[0] == "N":
            return None

        root = TreeNode(int(values[0]))
        queue = deque([root])
        i = 1

        while queue:
            node = queue.popleft()

            # Create left child
            if values[i] != "N":
                node.left = TreeNode(int(values[i]))
                queue.append(node.left)
            i += 1

            # Create right child
            if values[i] != "N":
                node.right = TreeNode(int(values[i]))
                queue.append(node.right)
            i += 1

        return root