""" NOTE: You can use Basic Implementation of BST given in README.MD. Here just definition of function is given """
""" Although this question is related to #Binary tree,but bst is also a kind of #Binary Tree """

##lowest-common-ancestor-of-a-binary-tree
def lowestCommonAncestor(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    if not root:
        return root
    if root==p or root==q:
        return root
    
    left=lowestCommonAncestor(root.left,p,q)
    right=lowestCommonAncestor(root.right,p,q)
    
    if left and right:
        return root
    if left==None and right==None:
        return None
    
    return left if left else right

lca=lowestCommonAncestor(bst.root,bst.root.left,bst.root.right)
print(lca.val)

"""OUTPUT
5
"""
