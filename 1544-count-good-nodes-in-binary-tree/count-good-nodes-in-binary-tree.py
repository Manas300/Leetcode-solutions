class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, max_so_far):
            if not node:
                return 0

            # Check if current node is good
            count = 1 if node.val >= max_so_far else 0

            # Update max_so_far for children
            new_max = max(max_so_far, node.val)

            # Recurse left and right
            count += dfs(node.left, new_max)
            count += dfs(node.right, new_max)

            return count

        return dfs(root, root.val)
