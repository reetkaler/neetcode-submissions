# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # lowest common ancestor is the first point where the two nodes' paths meet (can be one of the nodes too)
        # depth first search

        # each recursive call should return either the node it found or none if we hit none then return none
        # search left and right tree, if both are non null, the current node is not a leaf node

        # if we find p or q, return root bc either q is below p meaning that p is the LCA or q is somewhere else and root needs that information
        if root is None:
            return None
        if root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
        return left if left else right

        # time complexity is O(n) bc visiting every node
        # memory complexity is O(h) where h is the height of the tree bc of the call stack ?

