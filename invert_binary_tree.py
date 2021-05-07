#Given the root of a binary tree, invert the tree, and return its root.

#      1               1
#   2     3   ----> 3     2
#
# input [1,2,3]
# output [1,3,2]

# with recursion
def invertTree(self, root):
    """
    :type root: TreeNode
    :rtype: TreeNode
    """
    if root:
        left = root.left
        right = root.right
        root.left = right
        root.right = left
        
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root
