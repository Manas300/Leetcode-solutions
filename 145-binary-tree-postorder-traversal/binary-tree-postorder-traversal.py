class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        
        def dfs(node):
            if not node:
                return
            dfs(node.left)   # Visit left
            dfs(node.right)  # Visit right
            res.append(node.val)  # Visit root
        
        dfs(root)
        return res
