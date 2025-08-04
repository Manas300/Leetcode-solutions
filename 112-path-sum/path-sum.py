class Solution:
    def hasPathSum(self, root, targetSum):
        if not root:
            return False

        # If it's a leaf node
        if not root.left and not root.right:
            return targetSum == root.val

        # Check left and right
        left = self.hasPathSum(root.left, targetSum - root.val)
        right = self.hasPathSum(root.right, targetSum - root.val)
        return left or right