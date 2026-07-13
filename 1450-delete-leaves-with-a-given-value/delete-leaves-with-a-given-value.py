class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if not root:
            return None

        # Process left and right subtrees first
        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)

        # If current node becomes a leaf and equals target, delete it
        if root.left is None and root.right is None and root.val == target:
            return None

        return root