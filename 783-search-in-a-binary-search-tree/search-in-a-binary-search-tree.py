class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        # Base case: empty tree or value found
        if not root or root.val == val:
            return root
        
        # If value is smaller, search left subtree
        if val < root.val:
            return self.searchBST(root.left, val)
        
        # If value is larger, search right subtree
        return self.searchBST(root.right, val)
